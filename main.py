from flask import Flask, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route("/assignment-helper", methods=["POST"])
def assignment_helper():
    data = request.get_json()

    topic = data.get("topic")
    word_limit = data.get("word_limit", 1000)

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    result = run_agent(topic, word_limit)
    return jsonify({"result": result})

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
