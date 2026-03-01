# Web Enumeration — Command + Meaning

curl -I http://IP            # Show headers (server, redirects, cookies)
curl http://IP               # Fetch page content (CLI)

nikto -h http://IP           # Web vulnerability/misconfig scanner

gobuster dir -u http://IP -w WORDLIST   # Find hidden directories/files
# Example wordlist:
# /usr/share/wordlists/dirb/common.txt

# Burp Suite (intercept requests)
burpsuite                    # Start Burp
# Browser proxy: 127.0.0.1:8080
# Purpose: see/edit requests, cookies, parameters
