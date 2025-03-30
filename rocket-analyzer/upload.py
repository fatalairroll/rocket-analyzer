from flask import Flask, request, render_template
import os
from carl_parser import parse_replay
from gpt_prompt import generate_analysis

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    os.makedirs("uploads", exist_ok=True)
    file = request.files['file']
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    parsed_data = parse_replay(file_path)
    analysis = generate_analysis(parsed_data)

    return f"<pre>{analysis}</pre>"
