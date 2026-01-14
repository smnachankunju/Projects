🔐 Password Security Analyzer & Breach Checker

A Python-based cybersecurity tool that analyzes password strength, checks whether a password has appeared in known data breaches using privacy-preserving techniques, and securely hashes passwords using industry-standard algorithms.

📌 Features

🔒 Secure Password Input

Password is hidden during input (no terminal echo).

📊 Password Strength Analysis

Length evaluation

Character variety (uppercase, lowercase, digits, special characters)

Detection of:

Common passwords

Sequential patterns (1234, abcd, qwerty)

Repeated characters

Generates a score (0–100) with clear warnings.

🌐 Breach Detection (Privacy-Preserving)

Uses k-anonymity with SHA-1 hashing.

Only the first 5 characters of the hash are sent.

Password is never exposed to the internet.

🔑 Secure Password Hashing

Uses bcrypt for salted, slow hashing.

Demonstrates real-world password storage practices.

🧱 Modular Design

Clean separation of logic for analysis, breach checking, and hashing.
