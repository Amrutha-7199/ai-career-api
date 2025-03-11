import pandas as pd
import os

DATA_DIR = "data/"
JOB_FILES = ["job_postings.csv", "job_skills.csv", "job_summary.csv"]

def load_job_data():
    """Loads job listings, ensuring correct column mappings."""
    all_jobs = []

    for file in JOB_FILES:
        file_path = os.path.join(DATA_DIR, file)
        try:
            df = pd.read_csv(file_path, encoding="utf-8")

            print(f"🔍 Processing {file} - Columns: {df.columns.tolist()}")

            column_mapping = {
                "job_title": "title",
                "job": "title",
                "job_details": "description",
                "job_summary": "description",
                "got_summary": "description",
                "job_skills": "description",
                "search_position": "title"  
            }
            df.rename(columns=column_mapping, inplace=True)

            if "description" not in df.columns:
                df["description"] = df["title"] + " role at " + df["company"]

            if "title" in df.columns and "description" in df.columns:
                df.fillna({"description": "No description available"}, inplace=True)
                all_jobs.append(df[["title", "description"]])
            else:
                print(f"⚠️ Skipping {file} - 'title' or 'description' column missing.")

        except Exception as e:
            print(f"❌ Error loading {file}: {e}")

    if all_jobs:
        combined_jobs = pd.concat(all_jobs, ignore_index=True)
        print(f"✅ Successfully loaded {len(combined_jobs)} job listings!")
        return combined_jobs
    else:
        print("❌ No valid job data found!")
        return pd.DataFrame()
