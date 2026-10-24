from utils import call_ollama

def generate_titles(blog_content):
    """Generates 5 attractive titles for the blog."""
    prompt = (f"Based on the following blog content, generate exactly 5 attractive blog titles. "
              f"Provide just the numbered list of titles and nothing else.\n\nBlog Content:\n{blog_content}")
    
    titles = call_ollama(prompt)
    print("Suggested Titles\n")
    print(titles)
    print("\n")
    return titles
