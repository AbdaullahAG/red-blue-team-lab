<div align="center">

# 🔴🔵 Red/Blue Team Security Assessment Lab

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

---

## 📑 Table of Contents
- [🎯 Overview](#-overview)
- [🏗️ Lab Architecture](#️-lab-architecture)
- [👥 Team Roles](#-team-roles)
- [🎯 Vulnerabilities](#-vulnerabilities)
- [🔴 Red Team](#-red-team--attack-summary)
- [🔵 Blue Team](#-blue-team--detection--ir)
- [🛡️ Mitigation](#️-mitigation--code-fixes)
- [📁 Repository Structure](#-repository-structure)
- [📊 Git History](#-git-history)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚠️ Disclaimer](#️-disclaimer)
- [📚 References](#-references)

---

## 🎯 Overview

<div align="center">
  <img src="https://assets-v2.lottiefiles.com/64f08148cf6170918e10ca3516b8098c1e9e2c8c.gif" width="180" />
</div>

> **⚠️ Educational Purpose Only** — This project contains intentionally vulnerable code for cybersecurity training in a controlled lab environment.

This project simulates a complete real-world attack and defense lifecycle in a controlled lab environment. It was developed as part of the **Masar-NCSC (National Cyber Security Center)** cybersecurity training program.

The lab consists of three virtual machines simulating a **Target**, **Attacker**, and **SIEM system**. The project covers all phases from building a vulnerable application to attacking it, detecting the attacks, and remediating the vulnerabilities.

### 🎬 Attack Lifecycle

```text
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   BUILD     │───▶│   ATTACK    │───▶│   DETECT    │───▶│   DEFEND    │
│  (Blue)     │    │   (Red)     │    │  (Blue)     │    │  (Blue)     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
