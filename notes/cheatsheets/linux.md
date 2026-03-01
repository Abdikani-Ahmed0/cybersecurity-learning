# Linux Basics (Command + Meaning)

## Navigation
pwd                 # Print Working Directory (where am I?)
ls                  # List files/folders
ls -la              # Long list + show hidden files
cd DIR              # Change directory into DIR
cd ..               # Go back one folder
clear               # Clear terminal screen

## Files & Folders
touch file.txt      # Create an empty file
mkdir DIR           # Create a folder
rmdir DIR           # Remove an EMPTY folder
cp A B              # Copy file A to B
cp -r DIR1 DIR2     # Copy a folder recursively
mv A B              # Move/rename A to B
rm file.txt         # Delete a file
rm -r DIR           # Delete folder + contents (dangerous)

## Read Files
cat file.txt        # Print full file content
less file.txt       # Read file page-by-page (q to quit)
head file.txt       # First 10 lines
tail file.txt       # Last 10 lines
tail -f log.txt     # Follow a file live (logs)

## Search Text / Files
grep "word" file    # Search for "word" in file
grep -R "word" DIR  # Search inside all files in DIR
find / -name file   # Find file by name (slow)
locate file         # Find file using database (fast)
updatedb            # Update locate database (needs sudo)

## Help
man cmd             # Manual for a command
cmd --help          # Quick help/options

## Users & Privileges
whoami              # Show current user
id                  # Show user id + groups
sudo -l             # Show what I can run as sudo
su USER             # Switch user (needs password)
sudo cmd            # Run cmd as root/admin

## Permissions
chmod 777 file      # Give rwx to everyone (lab-only)
chmod +x script.sh  # Make script executable
chown u:u file      # Change owner:group

## Processes
ps aux              # List running processes
top                 # Live process monitor
kill PID            # Stop a process
kill -9 PID         # Force kill (last resort)

## Networking
ip a                # Show interfaces + IPs
ip route            # Show routing table/gateway
ping -c 3 IP        # Test connectivity (3 pings)
arp -a              # Show ARP table (local devices)
ss -tuln            # Show listening ports (modern netstat)
