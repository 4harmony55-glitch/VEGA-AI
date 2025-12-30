from flask import Flask, request, jsonify
from vega.brain import think

app = Flask("VEGA")

@app.route("/think", methods=["POST"])
def process_message():
    data = request.get_json()
    text = data.get("text", "")
    reply = think(text)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
