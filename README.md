# Cybersecurity Learning Journey

This repository documents my hands-on cybersecurity learning, labs, scripts, notes, and real exploit write-ups. It reflects my personal exploration, experimentation, and troubleshooting in a virtual lab environment.

---

## 📂 Repository Structure

### **Labs**

Practical exercises and vulnerable machine walkthroughs.
Includes step-by-step methodology, post-exploitation, and privilege escalation.

* **Kioptrix Level 1**

  * Enumeration & reconnaissance
  * Manual exploitation
  * Brute-force attacks with Hydra
  * Metasploit exploitation
  * Hashcat password cracking

* **Kioptrix Level 2**

  * SQL Injection → authentication bypass
  * Command Injection → Remote Shell
  * Reverse Shell setup
  * Linux Kernel Exploit → Root
  * Post-exploitation techniques (creating users, escalating privileges)

* **Basic LAN Lab**

  * Network topology using Packet Tracer
  * Router & host configuration
  * Simulated internal attack vectors

---

### **Notes**

Structured notes and cheat sheets covering concepts and tools.

Topics include:

* Linux fundamentals & administration
* Network scanning & reconnaissance (nmap, netdiscover, etc.)
* Web enumeration & vulnerability analysis
* Privilege escalation techniques
* Exploit development & troubleshooting

---

### **Python Scripts**

Custom scripts developed during learning.

Examples include:

* TCP/UDP port scanners
* Socket listeners for reverse shells
* Network utilities for reconnaissance

---

### **Bash Scripts**

Automation scripts for system and network tasks.

Example:

* IP sweep automation
* Logging and cleanup scripts

---

### **Recon**

Files and logs generated during reconnaissance.

Includes:

* Nmap scans
* Nikto outputs
* Netdiscover results
* SQL enumeration results

---

## ⚡ Skills Practiced

* Vulnerability enumeration & exploitation
* Reverse shells & remote command execution
* Privilege escalation & post-exploitation
* Password attacks & cracking
* Python scripting for security automation
* Linux command-line mastery

---

## 🖥 Platforms & Tools Used

* Kali Linux (attacker & pentesting OS)
* Virtual Lab Environments (Vagrant, VirtualBox, VMware)
* Vulnerable machines: Kioptrix Level 1 & 2
* Tools: nmap, nikto, netdiscover, Hydra, Metasploit, Hashcat, gcc, python

---

## 🚀 Key Lessons Learned

* Always validate file integrity before compilation or execution
* Reverse shells can fail due to syntax or network misconfiguration — debug step by step
* Post-exploitation is as important as root access: creating users, escalating privileges, exploring sensitive files
* Manual exploitation develops deeper understanding than relying solely on automated tools
* Combining multiple vectors (SQLi + command injection + reverse shell + kernel exploit) mirrors real-world penetration tests

---

## 🔗 Repository

[github.com/Abdikani-Ahmed0/cybersecurity-learning](https://github.com/Abdikani-Ahmed0/cybersecurity-learning)

---
