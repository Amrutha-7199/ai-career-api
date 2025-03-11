from flask import Blueprint, request, jsonify
from models.interview_questions import generate_questions

interview_bp = Blueprint("interview_bp", __name__)

@interview_bp.route("/generate_questions", methods=["POST"])
def interview_questions_api():
    """API to generate interview questions based on job title"""
    data = request.get_json()
    job_title = data.get("job_title", "")

    if not job_title:
        return jsonify({"error": "Job title is required"}), 400

    questions = generate_questions(job_title)
    return jsonify({"job_title": job_title, "questions": questions})
