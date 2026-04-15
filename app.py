from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from agent import run_agent
import os

app = Flask(__name__)
CORS(app)  # Allow frontend JavaScript to call this API


@app.route("/")
def index():
    """Serve the web UI."""
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():
    """
    Accepts: { "topic": "email marketing" }
    Returns: Full SEO intelligence JSON report
    """
    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Missing 'topic' in request body"}), 400

    topic = data["topic"].strip()

    if not topic:
        return jsonify({"error": "Topic cannot be empty"}), 400

    if len(topic) > 200:
        return jsonify({"error": "Topic too long (max 200 characters)"}), 400

    try:
        result = run_agent(topic)
        return jsonify(result), 200
    except Exception as e:
        print(f"[Error] {e}")
        return jsonify({"error": f"Agent failed: {str(e)}"}), 500


@app.route("/health")
def health():
    """Simple health check."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # IMPORTANT: Required for deployment (Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)