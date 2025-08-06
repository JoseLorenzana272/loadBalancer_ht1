import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

json_file = "info1.json"

@app.route('/check', methods=['GET'])
def check_status():
    return jsonify({"status": "ok"}), 200

@app.route('/info', methods=['GET'])
def get_info():
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 500

if __name__ == '__main__':
    app.run(port=5000)