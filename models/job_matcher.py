import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from utils.preprocess import load_job_data

# Load job data
job_data = load_job_data()

if "description" not in job_data.columns:
    raise ValueError("The dataset does not contain a 'description' column. Check the CSV structure.")

job_descriptions = job_data["description"].astype(str).tolist()

# Load Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Job Embeddings
job_embeddings = model.encode(job_descriptions, convert_to_numpy=True)

# Initialize FAISS index
index = faiss.IndexFlatL2(job_embeddings.shape[1])
index.add(job_embeddings)

def match_jobs(resume_text, top_k=5):
    """Finds the top K matching job descriptions for a given resume."""
    resume_embedding = model.encode([resume_text], convert_to_numpy=True)
    distances, indices = index.search(resume_embedding, top_k)
    matched_jobs = job_data.iloc[indices[0]]

    return matched_jobs.to_dict(orient="records")
