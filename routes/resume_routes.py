from flask import Blueprint, request, jsonify
from models.resume_parser import parse_resume

resume_bp = Blueprint("resume_bp", __name__)

@resume_bp.route("/parse_resume", methods=["POST"])
def parse_resume_api():
    """API to parse resume text"""
    data = request.get_json()
    resume_text = data.get("resume_text", "")

    if not resume_text:
        return jsonify({"error": "No resume text provided"}), 400

    parsed_data = parse_resume(resume_text)
    return jsonify(parsed_data)
