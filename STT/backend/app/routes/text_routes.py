from flask import Blueprint, request, jsonify
from services.t5_processor import process_text

text_bp = Blueprint("text", __name__)

@text_bp.route("/process", methods=["POST"])
def process():
    """Endpoint to process text (summarization, translation, etc.)."""
    data = request.get_json()
    input_text = data.get("text")
    task = data.get("task", "summarize")  # Default task: Summarization

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    output_text = process_text(input_text, task)
    return jsonify({"output": output_text})
