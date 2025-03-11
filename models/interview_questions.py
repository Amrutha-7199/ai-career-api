from transformers import pipeline

# Load a supported transformer model
generator = pipeline("text-generation", model="gpt2")

def generate_questions(job_title):
    """Generates interview questions based on job title"""
    prompt = f"Generate interview questions for a {job_title} role."
    
    # Use a supported model and generate only 1 sequence
    question = generator(prompt, max_length=100, num_return_sequences=1)
    
    return [question[0]["generated_text"]]
