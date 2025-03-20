from flask import Flask, request, send_file
from main import create_chart

app = Flask(__name__)

@app.route('/api/v1/plot-lab', methods=['POST'])
def generate_image():
    content = request.data.decode('utf-8')
    if not content:
        return "No text provided", 400

    # image_path = create_chart(content)
    image_path = "data/img/example.png"
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
