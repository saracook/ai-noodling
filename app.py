import sys
import os
import flask

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from services.huggingface import huggingface_service

app = Flask(__name__)

@app.route('/query/', methods=['POST'])
def get_response():
    data = request.get_json()
    user_query = data['user_query']

    response = huggingface_service.generate_text(user_query)
    output = response[0]['generated_text']

    return jsonify({"response": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)