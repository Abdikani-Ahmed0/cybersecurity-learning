# Metasploit — Command + Meaning

msfconsole                   # Start Metasploit framework
search smb                   # Search modules related to SMB
use MODULE                    # Select a module
show options                 # Required parameters for module
set RHOSTS IP                # Set target IP
set LHOST YOUR_IP            # Set callback IP (reverse shell)
run                          # Execute module

sessions -l                  # List active sessions
sessions -i 1                # Interact with session 1
background                   # Send session to background
