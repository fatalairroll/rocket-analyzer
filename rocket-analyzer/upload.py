from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    os.makedirs("uploads", exist_ok=True)  # Ensure the uploads folder exists
    file = request.files['file']
    file_path = f"uploads/{file.filename}"
    file.save(file_path)
    return f"File {file.filename} received and saved to {file_path}"
