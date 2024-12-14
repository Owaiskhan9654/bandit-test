import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return "Login successful"
    else:
        return "Login failed"


# Directory to save uploaded files
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the uploaded file
    file = request.files['file']
    if file:
        # Save the file without validation
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"File uploaded to {filepath}"
    return "No file uploaded"

if __name__ == "__main__":
    create_database()
    app.run(debug=True)
