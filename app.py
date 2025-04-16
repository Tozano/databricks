from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/logs')
def logs():
    with open('./data/logs.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run()