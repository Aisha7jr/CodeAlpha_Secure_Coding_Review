# SECURE CODING REVIEW — Task 3 (CodeAlpha Internship)

**Project reviewed:** vulnerable_app.py (simple Python application demo)  
**Reviewer:** Aisha Shaikh Sarvari  
**Date:** July 2025

## Summary
A small Python script was reviewed to identify common insecure coding practices. The script is intentionally vulnerable for learning. Issues found include use of `eval()`, hardcoded credentials, plaintext password handling, lack of input validation, and no rate limiting.

## Findings & Recommendations

### 1) Hardcoded Credentials (High)
**Issue:** Credentials are stored in source code in plaintext.  
**Risk:** Anyone with access to source can read passwords.  
**Recommendation:** Remove hardcoded credentials. Use a secure user store (database, secrets manager); store password hashes (bcrypt/argon2) not plaintext.

### 2) Plaintext Password Handling (High)
**Issue:** Passwords are compared in plaintext and read with input().  
**Risk:** Passwords can be exposed in terminal, logs, or memory.  
**Recommendation:** Use secure input (getpass), hash passwords, and compare hashes.

### 3) Use of `eval()` (Critical)
**Issue:** `eval()` executes arbitrary Python code from user input.  
**Risk:** Remote code execution (RCE), full system compromise.  
**Recommendation:** Avoid `eval()`. For evaluating expressions use `ast.literal_eval()` or implement a safe parser. Validate inputs strictly.

### 4) Lack of Input Validation (Medium)
**Issue:** Inputs are not validated for length/type.  
**Risk:** Unexpected behavior and potential exploitation.  
**Recommendation:** Enforce length limits, acceptable character sets, and strict parsing rules.

### 5) No Rate Limiting or Brute-force Protection (Medium)
**Issue:** Unlimited login attempts.  
**Risk:** Brute-force password attacks.  
**Recommendation:** Implement attempt counters, temporary lockouts, CAPTCHAs for web, or account throttling.

### 6) Missing Structured Logging / Error Handling (Low)
**Issue:** Errors printed directly; no structured logging.  
**Recommendation:** Use a logging framework, avoid leaking sensitive info in messages, and log failed attempts for monitoring.

## Remediation Steps
1. Replace hardcoded credentials; use hashed passwords and secure storage.  
2. Remove `eval()`; use `ast.literal_eval()` or other safe alternatives.  
3. Add input validation and sanitization.  
4. Implement rate limiting and account lockouts.  
5. Use secure input methods and add structured logging.  
6. Keep dependencies updated and perform dependency scanning.

## Conclusion
The reviewed script is suitable for training. Implementing the recommended changes will significantly reduce risk and align with secure coding best practices.
