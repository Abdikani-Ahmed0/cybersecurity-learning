## Kioptrix Level 1 — Reconnaissance & Enumeration

### Lab Environment

* Attacker Machine: Kali Linux
* Target Machine: Kioptrix Level 1
* Target IP: 192.168.3.129
* Network Type: Local Virtual Lab (VMware NAT)

---

### Step 1 — Full Port Scan

Command used:

```bash
nmap -T4 -p- -n --min-rate 1500 192.168.3.129 -oN ports.txt
```

Open ports discovered:

| Port  | Service       |
| ----- | ------------- |
| 22    | SSH           |
| 80    | HTTP          |
| 111   | RPCBind       |
| 139   | NetBIOS / SMB |
| 443   | HTTPS         |
| 32768 | RPC Service   |

---

### Step 2 — Service Enumeration

Command:

```bash
nmap -sC -sV -T4 -p22,80,111,139,443,32768 192.168.3.129 -oN service.txt
```

Key findings:

* Apache 1.3.20 (very outdated)
* OpenSSL 0.9.6b
* mod_ssl 2.8.4
* OpenSSH 2.9p2
* Samba 2.2.1a

---

### Web Enumeration (Port 80/443)

Observations:

* Default Apache test page
* Server information disclosure in 404 page
* Directory indexing found
* TRACE method enabled
* Possible file disclosure via malformed URL

Potential exploit:

* mod_ssl buffer overflow (OpenLuck exploit)

References:

* [https://www.exploit-db.com/exploits/47080](https://www.exploit-db.com/exploits/47080)
* [https://github.com/heltonWernik/OpenLuck](https://github.com/heltonWernik/OpenLuck)

---

### SMB Enumeration (Port 139)

Service:
Samba 2.2.1a

Potential vulnerability:
trans2open exploit

Reference:
[https://www.exploit-db.com/exploits/22468](https://www.exploit-db.com/exploits/22468)

---

### SSH Enumeration (Port 22)

Service:
OpenSSH 2.9p2 (protocol 1.99)

Notes:

* Very outdated SSH version
* Supports SSHv1 (insecure)

---

### Conclusion

The target system is highly outdated and exposes multiple attack surfaces:

* Vulnerable Apache + mod_ssl
* Vulnerable Samba service
* Weak SSH configuration

Primary attack vector likely: **mod_ssl remote exploit (OpenLuck)**.


