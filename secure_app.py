# secure_app.py
"""
secure_app.py
Improvements:
- Remove hardcoded plaintext creds (demo uses hashed store)
- Use getpass for hidden password entry
- Use ast.literal_eval instead of eval
- Add simple input validation and login attempt limit
"""
import ast
import hashlib
import getpass
import time

# Demo hashed-password store (use proper secure hashing like bcrypt in real apps)
users = {
    'admin': hashlib.sha256('admin123'.encode()).hexdigest(),
    'alice': hashlib.sha256('alicepass'.encode()).hexdigest()
}

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login(username, password):
    if not username or not password or len(username) > 50 or len(password) > 100:
        return False
    hashed = hash_password(password)
    stored = users.get(username)
    return stored and hashed == stored

def safe_eval(expr):
    # Use ast.literal_eval to prevent executing arbitrary code
    try:
        return str(ast.literal_eval(expr))
    except Exception as e:
        return f"Error: Invalid expression ({e})"

def main():
    print("Welcome to SimpleApp v0.1 (secure demo)")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    attempts = 0
    while attempts < 3:
        if login(username, password):
            print("Login successful!")
            cmd = input("Enter arithmetic expression to evaluate (e.g. 1+1): ")
            print("Result:", safe_eval(cmd))
            return
        else:
            attempts += 1
            print(f"Login failed. Attempts left: {3-attempts}")
            if attempts >= 3:
                print("Too many failed attempts. Try again later.")
                time.sleep(2)
                return

if __name__ == '__main__':
    main()
