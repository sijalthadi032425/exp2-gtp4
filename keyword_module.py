from utils import call_ollama

def generate_keywords(blog_content):
    """Generates SEO keywords for the blog."""
    prompt = (f"Extract SEO-friendly keywords from the following blog content. "
              f"List them clearly, one per line, with no extra formatting or text.\n\n"
              f"Blog Content:\n{blog_content}")
    
    keywords = call_ollama(prompt)
    print("SEO Keywords\n")
    print(keywords)
    print("\n")
    return keywords
