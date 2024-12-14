import subprocess
import pickle
import os

# 1. Hardcoded password
PASSWORD = "12345"



# 2. Subprocess with unsanitized input
def run_command(cmd):
    subprocess.run(cmd, shell=True)  # Vulnerable to command injection

# 3. Insecure pickle usage
def load_user_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)  # Vulnerable to code execution

# 4. Weak cryptographic algorithm
from hashlib import md5

def hash_password(password):
    return md5(password.encode()).hexdigest()  # Weak hash function

# Example usage
if __name__ == "__main__":
    print("Running vulnerable script...")
    run_command(input("Enter a command to run: "))  # Input not sanitized
    user_data = load_user_data("user_data.pkl")
    print("Loaded user data:", user_data)
    hashed = hash_password(PASSWORD)
    print(f"MD5 hashed password: {hashed}")
