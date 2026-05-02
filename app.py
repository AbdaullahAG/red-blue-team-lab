from flask import Flask, request, render_template, redirect, url_for, session
import os, subprocess, sqlite3
import logging

import urllib.request, json

def send_to_splunk(message, sourcetype="flask_app"):
    try:
        url = "http://192.168.255.133:8088/services/collector"
        token = "1d428a5c-7f67-429b-a991-de83a45a6011"
        data = json.dumps({"event": message, "sourcetype": sourcetype}).encode()
        req = urllib.request.Request(url, data=data, headers={"Authorization": f"Splunk {token}"})
        urllib.request.urlopen(req, timeout=2)
    except Exception as e:
        pass

from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


logging.basicConfig(
    filename='/var/log/vulnerable_app.log',
    level=logging.INFO,
    format='%(message)s'
)

@app.before_request
def log_request():
    log_entry = f'{request.remote_addr} - [{datetime.now().strftime("%d/%b/%Y %H:%M:%S")}] "{request.method} {request.path} HTTP/1.1"'
    logging.info(log_entry)
    send_to_splunk(log_entry)
# Send bash history to Splunk
try:
    with open('/var/log/bash_history.log', 'r') as f:
        for line in f.readlines()[-5:]:
            if line.strip():
                send_to_splunk(line.strip(), sourcetype="bash_history")
except:
    pass
# ========== HOME ==========
@app.route('/')
def index():
    return render_template('index.html')

# ========== 1. FILE UPLOAD (Vulnerable) ==========
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    msg = ''
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)
            msg = f'File uploaded: {f.filename}'
    return render_template('upload.html', msg=msg)

# ========== 2. OS COMMAND INJECTION (Vulnerable) ==========
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    output = ''
    if request.method == 'POST':
        host = request.form['host']
        output = subprocess.getoutput(f'ping -c 1 {host}')
    return render_template('ping.html', output=output)

# ========== 3. XSS (Vulnerable) ==========
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    msg = ''
    if request.method == 'POST':
        msg = request.form['comment']
    return render_template('comment.html', msg=msg)

# ========== 4. SQL INJECTION (Vulnerable) ==========
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        result = conn.execute(query).fetchone()
        if result:
            msg = f'Welcome {result[1]}!'
        else:
            msg = 'Invalid credentials'
    return render_template('login.html', msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
