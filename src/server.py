from flask import Flask, request, jsonify
import os

from antlr4 import *
from antlr.ChartLexer import ChartLexer
from antlr.ChartParser import ChartParser
from components.interpretor import *

app = Flask(__name__)

# Get base directory once at startup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'data', 'templates')
STATISTIC_DATA_DIR = os.path.join(BASE_DIR, 'data', 'statistic_data')

# Ensure directories exist
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATISTIC_DATA_DIR, exist_ok=True)

@app.route('/api/v1/get-chart', methods=['POST'])
def generate_image():
    content = request.get_json()
    if not content:
        return jsonify("No text provided"), 400

    json_list = create_chart(content["code"])
    if json_list is None:
        return jsonify("Internal Error: No json_list was returned."), 400

    return jsonify({"plots": json_list})

@app.route('/api/v1/get-templates', methods=['GET'])
def list_templates():
    files_content = []
    for filename in os.listdir(TEMPLATES_DIR):
        file_path = os.path.join(TEMPLATES_DIR, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    files_content.append({
                        "key": filename,
                        "code": file.read(),
                        "label": filename
                    })
            except Exception as e:
                files_content.append({
                    "key": filename,
                    "code": f"Error reading file: {str(e)}",
                    "label": filename
                })
    return jsonify(files_content)

@app.route('/api/v1/get-statistic-data', methods=['GET'])
def get_statistic_data():
    ALLOWED_EXTENSIONS = {'.csv', '.json', '.xml'}
    files_content = []
    
    for filename in os.listdir(STATISTIC_DATA_DIR):
        file_path = os.path.join(STATISTIC_DATA_DIR, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            try:
                if ext in ALLOWED_EXTENSIONS:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                else:
                    content = None
            except Exception as e:
                content = f"Error reading file: {str(e)}"
                
            files_content.append({
                "key": filename,
                "code": content,
                "label": filename
            })
    
    return jsonify(files_content)

@app.route('/api/v1/save-template', methods=['POST'])
def save_template():
    content = request.get_json()
    if not content or "filename" not in content or "code" not in content:
        return jsonify({"error": "Missing required data"}), 400
    
    # Sanitize filename to prevent path traversal
    filename = os.path.basename(content["filename"])
    if not filename:
        return jsonify({"error": "Invalid filename"}), 400
        
    file_path = os.path.join(TEMPLATES_DIR, filename)
    
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content["code"])
    except Exception as e:
        return jsonify({"error": f"Failed to save template: {str(e)}"}), 500

    return jsonify({"message": "Template saved successfully"}), 201

@app.route('/api/v1/save-statistic-data', methods=['POST'])
def save_statistic_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    filename = request.form.get('filename', file.filename)
    
    if not filename or file.filename == '':
        return jsonify({"error": "No valid filename provided"}), 400
    
    # Sanitize filename
    filename = os.path.basename(filename)
    file_path = os.path.join(STATISTIC_DATA_DIR, filename)
    
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500
    
    return jsonify({"message": "File saved successfully"}), 201

def create_chart(content):
    input_stream = InputStream(content)

    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ChartParser(token_stream)
    tree = parser.program()

    interpretor = Interpretor()
    json_list = interpretor.walk_tree(tree)
    return json_list

if __name__ == '__main__':
    app.run(debug=True, port=5001)