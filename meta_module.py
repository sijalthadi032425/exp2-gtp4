from utils import call_ollama

def generate_meta_description(blog_content):
    """Generates a meta description for the blog under 160 characters."""
    prompt = (f"Generate a single SEO Meta Description for the following blog content. "
              f"It must be strictly under 160 characters. Do not include any extra text or quotes.\n\n"
              f"Blog Content:\n{blog_content}")
    
    meta = call_ollama(prompt)
    print("Meta Description\n")
    print(meta)
    print("\n")
    return meta
