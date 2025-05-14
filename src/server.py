from flask import Flask, request, send_file, jsonify
from main import create_chart
import os

app = Flask(__name__)

@app.route('/api/v1/plot-lab', methods=['POST'])
def generate_image():
    content = request.get_json()
    if not content:
        return jsonify("No text provided", 400)

    json_path = create_chart(content["code"])
    if json_path is None:
        json_path = "data/img/no-image.png"

    return send_file(
        json_path,
        mimetype='application/json',
        as_attachment=False
    )

@app.route('/api/v1/files', methods=['GET'])
def list_files():
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

@app.route('/api/v1/save-templates', methods=['POST'])
def save_template():
    content = request.get_json()
    if not content:
        return jsonify({"error": "No data provided"}), 400
    
    file_path = os.path.join("data/templates", content["filename"])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content["code"])

    return jsonify({"message": "Template saved successfully"}), 201

@app.route('/api/v1/save-data', methods=['POST'])
def save_data():
    content = request.get_json()
    if not content:
        return jsonify({"error": "No data provided"}), 400
    
    file_path = os.path.join("data/statistic_data", content["filename"])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content["code"])

    return jsonify({"message": "Input data saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)