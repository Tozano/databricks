from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/logs')
def logs():
    with open('./data/logs.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)