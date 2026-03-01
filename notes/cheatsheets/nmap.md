# Nmap — Command + Meaning

nmap IP                     # Basic scan (common ports)
nmap -p- IP                 # Scan ALL 65535 ports
nmap -sS IP                 # SYN scan (stealthy, common)
nmap -sV IP                 # Detect service versions (critical for exploits)
nmap -O IP                  # Guess OS (needs privileges)
nmap -A IP                  # Aggressive: OS + version + scripts + traceroute
nmap -sC IP                 # Default scripts (safe useful scripts)
nmap -T4 IP                 # Faster timing (good for labs)
nmap -Pn IP                 # Skip ping (use if host blocks ICMP)
nmap -sU IP                 # UDP scan (slow but useful)

## Discovery (find live hosts)
nmap -sn 192.168.1.0/24     # Ping sweep (who is alive)

## Output saving
nmap -oN scan.txt IP        # Save normal output
nmap -oA fullscan IP        # Save all formats (nmap/gnmap/xml)

## important commands
step 1
nmap -T4 -p- -n --min-rate 1500 192.168.3.129 -oN ports.txt

step 2
nmap -sC -sV -T4 -p22,80,111,139,443,32768 192.168.3.129 -oN service.txt
