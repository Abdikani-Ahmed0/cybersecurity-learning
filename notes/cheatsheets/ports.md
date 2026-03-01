# Common Ports (Port -> What it is)

21   FTP      # File transfer (often weak/anonymous)
22   SSH      # Remote login (banner/version matters)
23   Telnet   # Insecure remote login (cleartext)
25   SMTP     # Sending email
53   DNS      # Domain lookup (UDP/TCP)
67/68 DHCP    # Gives IPs automatically
69   TFTP     # Simple file transfer (often misconfigured)
80   HTTP     # Web
110  POP3     # Email inbox download
139  NetBIOS  # Old Windows networking
143  IMAP     # Email inbox access
161  SNMP     # Network device management (info leaks)
389  LDAP     # Directory services (AD)
443  HTTPS    # Secure web
445  SMB      # Windows shares (very common vuln area)
3306 MySQL    # Database
3389 RDP      # Windows remote desktop
