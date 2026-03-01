# Linux Privilege Escalation — Command + Meaning

whoami                       # Current user
id                           # Groups (look for admin groups)
uname -a                     # Kernel info (possible kernel exploits)
sudo -l                      # Check allowed sudo commands (common privesc)

find / -perm -4000 2>/dev/null   # Find SUID binaries (run as root)
find / -writable 2>/dev/null     # Find writable files (bad configs)

cat /etc/passwd              # User list (not passwords)
cat /etc/shadow              # Password hashes (root-only usually)
cat /etc/crontab             # Scheduled jobs (may run as root)

# LinPEAS (enumeration script)
# (Use only in your labs/authorized targets)
chmod +x linpeas.sh
./linpeas.sh
