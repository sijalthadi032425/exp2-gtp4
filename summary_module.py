from utils import call_ollama

def generate_summary(blog_content):
    """Generates a 100-word summary of the blog."""
    prompt = (f"Summarize the following blog content in exactly 100 words.\n\n"
              f"Blog Content:\n{blog_content}")
    
    summary = call_ollama(prompt)
    print("Summary\n")
    print(summary)
    print("\n")
    return summary
