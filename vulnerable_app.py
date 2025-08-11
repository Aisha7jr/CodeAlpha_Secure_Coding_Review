# vulnerable_app.py
"""
Simple vulnerable Python script (example for review)
- Hardcoded credentials
- Plaintext password comparison
- Uses eval() on user input (dangerous)
- No input validation or rate limiting
"""
users = [
    {'username': 'admin', 'password': 'admin123'},  # hardcoded credential
    {'username': 'alice', 'password': 'alicepass'}
]

def login(username, password):
    # insecure: plaintext password comparison
    for u in users:
        if u['username'] == username and u['password'] == password:
            return True
    return False

def run_command(cmd):
    # dangerous use of eval - allows arbitrary code execution
    try:
        result = eval(cmd)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to SimpleApp v0.1 (vulnerable demo)")
    username = input("Username: ")
    password = input("Password: ")
    if login(username, password):
        print("Login successful!")
        cmd = input("Enter expression to evaluate (e.g. 1+1): ")
        print(run_command(cmd))
    else:
        print("Login failed.")

if __name__ == '__main__':
    main()
