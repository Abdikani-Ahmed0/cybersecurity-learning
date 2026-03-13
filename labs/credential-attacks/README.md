# Credential Attacks Lab

This lab demonstrates two authentication attacks commonly tested during security assessments:

- Credential Stuffing
- Password Spraying

The goal of this exercise was to understand how authentication systems process login requests and how attackers attempt to abuse them.

## Tools Used

- Kali Linux
- Burp Suite
- FoxyProxy
- Bash scripting

## Step 1 – Generate Test Credentials

A bash script was used to generate a simulated dataset of email and password combinations.

Script location:

../../bash/generate.sh

Example output:

user1@example.com:Password1
user2@example.com:Password2
user3@example.com:Password3

## Step 2 – Split Credentials

The master credential file was separated into two lists.

users.txt
passwords.txt

Commands used:

cut -d: -f1 master.txt > users.txt
cut -d: -f2 master.txt > passwords.txt

## Step 3 – Intercept Authentication Request

Burp Suite was used to intercept the login request and identify the parameters:

email
password

These parameters were then used to understand how credential attacks interact with the login system.

## Attacks Practiced

### Credential Stuffing

Testing known email:password combinations from a dataset.

### Password Spraying

Testing a small set of common passwords across many user accounts.

## Disclaimer

All testing was performed in a controlled lab environment for educational purposes only.
