import pandas as pd

# Load dataset
file_path = "data/job_postings.csv"
job_data = pd.read_csv(file_path, encoding="utf-8")

# Print available columns for debugging
print("📌 Available Columns in Dataset:", job_data.columns.tolist())

# Define expected columns and provide alternatives if missing
expected_columns = {
    "job_title": ["job_title"],
    "job_details": ["description", "got_summary", "job_summary"]  # Possible alternatives
}

# Ensure required columns exist, filling in from alternatives if missing
for col, alternatives in expected_columns.items():
    found_col = None
    for alt in alternatives:
        if alt in job_data.columns:
            found_col = alt
            break

    if found_col:
        job_data[col] = job_data[found_col]
        print(f"✅ Using '{found_col}' as '{col}'")
    else:
        job_data[col] = ""  # Fill missing column with empty values
        print(f"⚠️ Warning: '{col}' column not found. Creating an empty column.")

# Drop rows with missing required values
job_data = job_data.dropna(subset=["job_title", "job_details"])

# Print sample data for verification
print("📌 Sample Data After Fixing Columns:")
print(job_data.head())

