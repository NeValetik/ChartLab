from flask import Flask, request, jsonify
import os

from antlr4 import *
from antlr.ChartLexer import ChartLexer
from antlr.ChartParser import ChartParser
from components.interpretor import *

app = Flask(__name__)

@app.route('/api/v1/get-chart', methods=['POST'])
def generate_image():
    content = request.get_json()
    if not content:
        return jsonify("No text provided", 400)

    json_list = create_chart(content["code"])
    if json_list is None:
        return jsonify("Internal Error: No json_list was returned.", 400)

    return jsonify({"plots": json_list})

@app.route('/api/v1/get-templates', methods=['GET'])
def list_templates():
    files_content = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_path = "data/templates"
    repo_path = os.path.join(script_dir, repo_path)
    for filename in os.listdir(repo_path):
        file_path = os.path.join(repo_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                files_content.append({"key":filename, "code": file.read(), "label":filename})
    return jsonify(files_content)

@app.route('/api/v1/get-statistic-data', methods=['GET'])
def list_statistic_data():
    files_content = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_path = "data/statistic-data"
    repo_path = os.path.join(script_dir, repo_path)
    for filename in os.listdir(repo_path):
        files_content.append({"key":filename})
    return jsonify(files_content)

@app.route('/api/v1/save-template', methods=['POST'])
def save_template():
    content = request.get_json()
    if not content:
        return jsonify({"error": "No data provided"}), 400
    
    file_path = os.path.join("src/data/templates", content["filename"])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content["code"])

    return jsonify({"message": "Template saved successfully"}), 201

@app.route('/api/v1/save-statistic-data', methods=['POST'])
def save_statistic_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filename = request.form.get('filename', file.filename)
    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    save_dir = "src/data/statistic_data"
    file_path = os.path.join(save_dir, filename)
    file.save(file_path)
    
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