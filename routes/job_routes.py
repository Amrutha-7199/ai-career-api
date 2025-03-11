from flask import Blueprint, request, jsonify
from models.job_matcher import match_jobs

job_bp = Blueprint("job_bp", __name__)

@job_bp.route("/match_jobs", methods=["POST"])
def match_jobs_api():
    """API to match jobs based on resume"""
    data = request.get_json()
    resume_text = data.get("resume_text", "")

    if not resume_text:
        return jsonify({"error": "No resume text provided"}), 400

    matched_jobs = match_jobs(resume_text)
    return jsonify(matched_jobs)
