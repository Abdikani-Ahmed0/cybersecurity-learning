# Recon (Information Gathering) — Command + Meaning

## Identify Your Network
ip a                         # Find your IP/subnet
ip route                     # Find default gateway + routes

## DNS / Domain Info
whois target.com             # Domain registration info
nslookup target.com          # Basic DNS query
dig target.com               # Detailed DNS query

## Subdomain Discovery
theHarvester -d target.com -b google   # Emails/subdomains via search engines
sublist3r -d target.com                # Find subdomains quickly
amass enum -d target.com               # Deep subdomain enumeration (best)

## Technology Fingerprinting
whatweb https://target.com             # Detect server/CMS/tech stack
# Wappalyzer (browser extension)       # Shows tech stack on websites

## Google Dorking (OSINT)
site:target.com                        # Search only inside the domain
site:target.com -www                   # Find subdomains / non-www pages
site:target.com filetype:pdf           # Find PDFs (sometimes leaks)
site:target.com inurl:login            # Find login portals
intitle:"index of" target.com          # Find open directories

## Breach / Leaks (safe mention)
haveibeenpwned.com                      # Check if email appeared in breaches
intelx.io                               # Search leaked data (paid features)
