Cybersecurity Toolkit: Web Scanning & Password Security
This repository is a collection of Python-based cybersecurity tools designed to automate vulnerability detection and promote secure credential management. It contains two primary modules: an Automated Web Vulnerability Scanner and a Password Security Analyzer.

Project Overview
1. Automated Web Vulnerability Scanner
A dynamic analysis tool that crawls web applications to identify security flaws in real-time.

Core Function: Automatically discovers form-based inputs and tests them against common attack vectors.

Key Vulnerabilities: Detects Reflected XSS and SQL Injection (SQLi).

Reporting: Generates structured HTML reports for security auditing.

2. Password Security Analyzer & Breach Checker
A privacy-first utility for evaluating and securing user credentials.

Core Function: Analyzes password complexity and checks for historical exposure in data breaches.

Privacy: Implements k-anonymity using the HaveIBeenPwned API (only sending the first 5 characters of a SHA-1 hash).

Storage: Demonstrates secure hashing using the bcrypt algorithm.
