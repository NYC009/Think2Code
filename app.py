from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    # Dummy generated code based on prompt
    code = f"# Python code generated for prompt: {prompt}\n\ndef hello_world():\n    print('Hello, World!')"
    return jsonify({'code': code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
