# Hashcat Password Cracking – Kioptrix Level 1

## Objective
Crack Linux password hashes obtained from the system using offline password cracking.

## Tool Used
- Hashcat

## Hash Source
Hashes were obtained from an `unshadow` file after accessing the machine.

Example format:

root:$1$XROmcfDX$tF93GqnLHOJeGRHpaNyIs0
john:$1$zL4.MR4t$26N4YpTGceBO0gTX6TAky1
harold:$1$Xx6dZdOd$IMOGACl3r757dv17LZ9010
hacker:$1$OOrOULwg$myiVNUetfTD54mSg61GB3/

## Hash Identification

The prefix:

$1$

Indicates:

Unix **MD5Crypt**

Hashcat mode used:

-m 500


## Command Used


hashcat -D 1 -m 500 --username unshadow.txt rockyou.txt


### Explanation

- `-D 1` → Use CPU device
- `-m 500` → MD5Crypt hash type
- `--username` → Ignore usernames before hashes
- `unshadow.txt` → Hash file
- `rockyou.txt` → Wordlist

## Result

Recovered:


hacker:hacker


## Lessons Learned

- Always identify hash type before cracking
- Correct hashcat mode is critical
- Wordlist size impacts cracking success
- Troubleshooting tools is part of cybersecurity practice
