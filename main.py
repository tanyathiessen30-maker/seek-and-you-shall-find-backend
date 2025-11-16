from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

KJV_BIBLE = {
    "John 3:16": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.",
    "Psalm 23:1": "The Lord is my shepherd; I shall not want."
}

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").lower()

    for ref, verse in KJV_BIBLE.items():
        if any(word in verse.lower() for word in question.split()):
            return jsonify({"answer": f"{ref} — {verse}"})
    
    return jsonify({"answer": "No verse found matching your question."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
