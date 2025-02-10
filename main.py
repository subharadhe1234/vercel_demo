from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Flask app deployed successfully on Vercel!"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Flask!"})

def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run()
