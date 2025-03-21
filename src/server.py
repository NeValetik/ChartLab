from flask import Flask, request, send_file, jsonify
import os
from main import create_chart

app = Flask(__name__)

@app.route('/api/v1/plot-lab', methods=['POST'])
def generate_image():
    content = request.data.decode('utf-8')
    print(content)
    # if not content:
    #     return "No text provided", 400

    # image_path = create_chart(content)
    image_path = "data/img/example.png"
    return send_file(image_path, mimetype='image/png')

@app.route('/api/v1/files', methods=['GET'])
def list_files():
    repo_path = "data/templates"
    if not os.path.exists(repo_path):
        return "Repository not found", 404
    
    files_content = []
    for filename in os.listdir(repo_path):
        file_path = os.path.join(repo_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                files_content.append({"key":filename,"code": file.read(), "label":filename})
    return jsonify(files_content)

if __name__ == '__main__':
    app.run(debug=True, port=5001)