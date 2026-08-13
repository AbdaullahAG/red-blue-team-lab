# 🔴🔵 Red / Blue Team Security Assessment Lab

<p align="center">
  <img src="./assets/red-blue-team-banner.gif" alt="Red Blue Team Security Assessment Lab" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.5-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![Splunk](https://img.shields.io/badge/SIEM-Splunk-000000?style=for-the-badge\&logo=splunk\&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge\&logo=kalilinux\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Security](https://img.shields.io/badge/Cybersecurity-Red%20%2F%20Blue%20Team-E53935?style=for-the-badge)

</p>

<p align="center">
  <b>Offensive Security × Defensive Security × Incident Response</b>
</p>

<p align="center">
  <i>A controlled cybersecurity laboratory demonstrating the complete attack → detection → response → remediation lifecycle.</i>
</p>

---

## ⚠️ Educational Use Only

> **This project is intentionally vulnerable and exists exclusively for cybersecurity education, penetration-testing practice, detection engineering, and incident-response training.**
>
> Never expose the vulnerable version to an untrusted network or deploy it in production.

---

# 🧭 Overview

This project implements a **full Red Team / Blue Team security assessment lab** in an isolated virtual environment.

The lab simulates a realistic attack lifecycle:

```text
Reconnaissance
      │
      ▼
Enumeration
      │
      ▼
Exploitation
      │
      ▼
Initial Access
      │
      ▼
Remote Code Execution
      │
      ▼
┌──────────────────────┐
│   BLUE TEAM ACTION   │
├──────────────────────┤
│ Log Collection       │
│ Detection            │
│ Investigation        │
│ Timeline Analysis    │
│ Containment          │
│ Remediation          │
└──────────────────────┘
      │
      ▼
Re-Exploitation Test
      │
      ▼
    VERIFIED
    PATCHED
```

The project was developed as part of the **Masar-NCSC Cybersecurity Training Program — 2026**.

---

# 🏗️ Lab Architecture

```text
                         ┌─────────────────────────┐
                         │      🔴 RED TEAM        │
                         │                         │
                         │      Kali Linux         │
                         │                         │
                         │ Nmap / Gobuster / curl  │
                         │ Netcat / Enumeration    │
                         └────────────┬────────────┘
                                      │
                              Exploitation
                              Reverse Shell
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     🎯 TARGET VM                            │
│                                                             │
│                    192.168.255.128                           │
│                                                             │
│              Kali Linux + Flask Application                 │
│                                                             │
│   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐      │
│   │  SQLi   │ │   XSS   │ │  CMDi   │ │ File Upload │      │
│   └─────────┘ └─────────┘ └─────────┘ └─────────────┘      │
│                                                             │
│                     Splunk Forwarder                        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               │ Logs / HEC
                               ▼
                    ┌─────────────────────────┐
                    │      🔵 BLUE TEAM      │
                    │                         │
                    │     Ubuntu Server       │
                    │                         │
                    │     Splunk 9.2.1        │
                    │     SIEM / Detection     │
                    │                         │
                    │     192.168.255.133      │
                    └─────────────────────────┘
```

### Virtual Machines

| VM  | Role        | IP Address        | Platform            |
| --- | ----------- | ----------------- | ------------------- |
| VM1 | 🎯 Target   | `192.168.255.128` | Kali Linux + Flask  |
| VM2 | 🔵 SIEM     | `192.168.255.133` | Ubuntu Server 24.04 |
| VM3 | 🔴 Attacker | `192.168.255.134` | Kali Linux          |

---

# 🔥 Attack Surface

The vulnerable Flask application intentionally exposes four major web vulnerabilities:

| #  | Vulnerability               | Endpoint   | Severity    | Final Status |
| -- | --------------------------- | ---------- | ----------- | ------------ |
| 01 | 📁 Unrestricted File Upload | `/upload`  | 🔴 Critical | ✅ Patched    |
| 02 | 💻 OS Command Injection     | `/ping`    | 🔴 Critical | ✅ Patched    |
| 03 | 🌐 Cross-Site Scripting     | `/comment` | 🟠 High     | ✅ Patched    |
| 04 | 🗄️ SQL Injection           | `/login`   | 🔴 Critical | ✅ Patched    |

---

# 🔴 Red Team Operations

## 01 — Reconnaissance

The assessment begins with network and service discovery.

```bash
nmap -sV -sC 192.168.255.128 -p- --open
```

### Directory Enumeration

```bash
gobuster dir \
-u http://192.168.255.128:5000 \
-w /usr/share/wordlists/dirb/common.txt
```

The objective is to identify:

* Open ports
* Running services
* Web application endpoints
* Hidden directories
* Potential attack surfaces

---

# 💥 Exploitation

## Cross-Site Scripting — XSS

A controlled XSS payload was submitted to the comment functionality:

```html
<script>alert('XSS')</script>
```

**Result:**
The vulnerable implementation rendered attacker-controlled input without appropriate output encoding.

---

## SQL Injection

The login functionality was tested using:

```text
Username: ' OR 1=1 --
Password: anything
```

**Result:**
The original application constructed SQL statements through unsafe string concatenation.

---

## OS Command Injection

The `/ping` endpoint was tested with controlled command injection.

```text
127.0.0.1; python3 /home/kali/vulnerable_app/uploads/shell.py
```

A listener was prepared on the attacker machine:

```bash
nc -lvnp 5555
```

**Result:**

```text
Remote Code Execution achieved
          ↓
Reverse Shell established
          ↓
Target system compromised
```

---

# 📁 File Upload Attack

The upload functionality was assessed for insufficient file-type validation and executable content handling.

The vulnerable implementation allowed files to reach the application's upload directory without sufficiently restricting dangerous extensions.

**Security impact:**

```text
Untrusted File
      ↓
Upload
      ↓
Target Filesystem
      ↓
Potential Code Execution
```

---

# 🔵 Blue Team Operations

The defensive phase focuses on transforming raw application activity into actionable security telemetry.

### Detection Pipeline

```text
Flask Application
       │
       ▼
Application Logs
       │
       ▼
Splunk Forwarder
       │
       ▼
Splunk SIEM
       │
       ├── Detection
       ├── Investigation
       ├── Timeline Reconstruction
       └── Incident Response
```

---

# 🕵️ Splunk Detection Queries

## File Upload Detection

```splunk
index=main sourcetype=flask_app "POST /upload"
| eval attack="Malicious File Upload Attempt"
| table _time, _raw, attack
```

## XSS Detection

```splunk
index=main sourcetype=flask_app "POST /comment"
| eval attack="XSS Attempt"
| table _time, _raw, attack
```

## Command Injection Detection

```splunk
index=main sourcetype=flask_app "POST /ping"
| eval attack="Command Injection Attempt"
| table _time, _raw, attack
```

## SQL Injection Detection

```splunk
index=main sourcetype=flask_app "POST /login"
| eval attack="SQL Injection Attempt"
| table _time, _raw, attack
```

---

# 🛡️ Remediation

The second stage of the assessment applies security controls and validates them through re-exploitation.

---

## 📁 Secure File Upload

```python
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'
}

def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )
```

---

## 💻 Command Injection Mitigation

Input validation is applied before allowing a host value to reach the command execution layer.

```python
import re

if re.match(r'^[a-zA-Z0-9.\-]+$', host):
    output = subprocess.getoutput(
        f'ping -c 1 {host}'
    )
else:
    output = 'Error: Invalid host!'
```

> **Note:** In production systems, avoiding shell invocation entirely and using a structured subprocess API is preferable to relying only on input filtering.

---

## 🌐 XSS Mitigation

### Vulnerable

```html
{{ msg | safe }}
```

### Patched

```html
{{ msg }}
```

The patched version allows the template engine to perform the appropriate HTML escaping instead of explicitly marking user input as safe.

---

## 🗄️ SQL Injection Mitigation

### Vulnerable

```python
query = f"""
SELECT * FROM users
WHERE username='{username}'
AND password='{password}'
"""
```

### Patched

```python
query = """
SELECT * FROM users
WHERE username=?
AND password=?
"""

result = conn.execute(
    query,
    (username, password)
).fetchone()
```

Parameterized queries separate **data from SQL instructions**, preventing attacker-controlled input from becoming part of the SQL statement.

---

# 🔁 Security Validation Cycle

The project follows a continuous offensive/defensive workflow:

```text
        ┌──────────────────┐
        │   🔴 ATTACK      │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   📡 DETECT      │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   🔎 INVESTIGATE │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   🛡️ REMEDIATE   │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   🔄 RE-TEST     │
        └────────┬─────────┘
                 │
                 └───────────────► SECURE
```

---

# 📊 Security Assessment Matrix

| Attack            | Initial State | Detection | Remediation | Re-Test |
| ----------------- | ------------- | --------- | ----------- | ------- |
| File Upload       | 🔴 Vulnerable | ✅ Logged  | ✅ Patched   | ✅       |
| Command Injection | 🔴 Vulnerable | ✅ Logged  | ✅ Patched   | ✅       |
| XSS               | 🟠 Vulnerable | ✅ Logged  | ✅ Patched   | ✅       |
| SQL Injection     | 🔴 Vulnerable | ✅ Logged  | ✅ Patched   | ✅       |

---

# 📁 Repository Structure

```text
red-blue-team-lab/
│
├── app.py
├── users.db
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── ping.html
│   ├── comment.html
│   └── login.html
│
├── uploads/
│
├── assets/
│   └── red-blue-team-banner.gif
│
└── README.md
```

---

# 🧰 Technology Stack

| Category           | Technology              |
| ------------------ | ----------------------- |
| Application        | Python / Flask 3.1.5    |
| Database           | SQLite3                 |
| Offensive OS       | Kali Linux              |
| SIEM               | Splunk Enterprise 9.2.1 |
| Log Collection     | Splunk Forwarder        |
| Event Ingestion    | Splunk HEC              |
| SIEM OS            | Ubuntu Server 24.04 LTS |
| Network Security   | Nmap                    |
| Enumeration        | Gobuster                |
| Shell / Networking | Netcat / cURL           |
| Version Control    | Git                     |

---

# 🧠 Security Concepts Demonstrated

This lab provides practical exposure to:

* 🔴 Red Team methodology
* 🔵 Blue Team operations
* 🌐 Web application security
* 💥 Exploitation
* 🕵️ Detection Engineering
* 📊 SIEM monitoring
* 🔎 Log analysis
* 🚨 Incident Response
* 🛡️ Vulnerability Remediation
* 🔁 Security Validation
* 🧪 Controlled Penetration Testing
* 🌐 OWASP Top 10 concepts
* 🗂️ Git-based security workflow

---

# 📚 References

* OWASP Top 10
* Splunk Documentation
* Flask Documentation
* Nmap Documentation

---

# 👨‍💻 Author

<p align="center">

<b>Abdallah Abughallous</b>

<br>

Cybersecurity • Network Engineering • AI Security

<br><br>

Developed as part of the <b>Masar-NCSC Cybersecurity Training Program — 2026</b>

</p>

---

## ⚠️ Final Disclaimer

This repository is intended strictly for **authorized cybersecurity education and controlled laboratory environments**.

The vulnerable application is intentionally insecure.

**Do not deploy the vulnerable version on public networks, production infrastructure, or systems you do not own or have explicit authorization to test.**

---

<p align="center">
  <sub>Built for learning offensive security by understanding defensive security.</sub>
</p>
