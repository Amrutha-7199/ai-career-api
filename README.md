AI-Powered Job Search Assistant 
Enhancing Job Recommendations, Resume Optimization & Interview Preparation with AI
Project Overview
This project is an AI-powered job search assistant that utilizes Deep Learning, Transformers, and FAISS-based search models to streamline job recommendations, resume parsing, and interview preparation.

Key Features:
AI-Driven Job Matching – Matches resumes with job descriptions using semantic similarity models.
Resume Parsing & Optimization – Extracts skills, experience, and job relevance using NLP-based techniques.
AI-Generated Interview Questions – Uses LLMs (GPT-4, T5, LLaMA) to generate job-specific questions.
Real-Time Job Fetching – Fetches job listings via LinkedIn API, Kaggle datasets, and preprocessed CSV files.
FAISS-Based Search – Uses vector embeddings for fast and accurate job recommendations.

Project Structure

job_search_backend/
│── app.py                # Main Flask application
│── requirements.txt       # Dependencies for the project
│── README.md              # Documentation
│── config.py              # Configuration settings (API keys, database)
│── models/
│   ├── job_matcher.py     # FAISS-based job matching model
│   ├── resume_parser.py   # NLP model for resume analysis
│   ├── question_generator.py  # AI-based interview question generator
│── routes/
│   ├── job_routes.py      # API routes for job search
│   ├── resume_routes.py   # API routes for resume parsing
│── data/
│   ├── job_postings.csv    # Dataset for job listings
│   ├── job_skills.csv      # Job skills dataset
│   ├── job_summary.csv     # Job descriptions dataset
│── static/                # Frontend assets (if applicable)
│── templates/             # HTML templates for UI (if applicable)
│── tests/                 # Unit tests for API & models

Installation & Setup
Create & Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

Install Dependencies

pip install -r requirements.txt
Run the Flask API


python app.py

flask run --debug
API Endpoints
The following API endpoints are available for interaction:

1. Job Matching
Endpoint:

POST /api/match_jobs
Description: Matches user resumes with relevant job postings.

Request Body (JSON):

{
  "resume_text": "Experienced Data Scientist with expertise in NLP and AI."
}
Response:

[
  {"title": "Senior Machine Learning Engineer"},
  {"title": "Principal Software Engineer, ML Accelerators"}
]
2. AI-Generated Interview Questions
Endpoint:


POST /api/generate_questions
Description: Generates interview questions based on job title.

Request Body (JSON):

{
  "job_title": "Data Scientist"
}
Response:


[
  "Can you explain how a Random Forest model works?",
  "What techniques do you use for feature engineering?"
]
3. Resume Parsing
Endpoint:

POST /api/parse_resume
Description: Extracts skills and experience from the provided resume.

Request Body (JSON):

{
  "resume_text": "5 years of experience in machine learning and data science."
}
Response:

{
  "skills": ["Machine Learning", "Data Science"],
  "experience": "5 years"
}

Technologies Used
Backend: Flask (Python)
AI Models: FAISS, Transformers (BERT, GPT-4, T5)
Data Processing: Pandas, SQLAlchemy
Database: PostgreSQL / MySQL (for job storage)
Cloud Deployment: Azure / AWS (Optional)
Security: OAuth 2.0 & JWT-based authentication
Future Improvements
Fine-tune AI models with more diverse datasets.
Improve job ranking accuracy by incorporating user feedback learning.
Expand job data sources by integrating real-time job listings APIs (LinkedIn, Indeed).



Contributors
Team Member A – Implemented FAISS-based job matching & API optimization.
Team Member B – Developed NLP-based interview question generator.
Team Member C – Preprocessed datasets & handled Flask integration.
