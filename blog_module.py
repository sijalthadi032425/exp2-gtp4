from utils import call_ollama

def generate_blog(inputs):
    """Generates a complete blog based on user inputs."""
    prompt = (f"Write a {inputs['word_count']}-word blog on '{inputs['topic']}'. "
              f"The writing style should be {inputs['style']} and the tone should be {inputs['tone']}. "
              "Include an Introduction, Main Content, and Conclusion.")
    
    print("Generating Blog...\n----------------------------------------")
    blog_content = call_ollama(prompt)
    print(blog_content)
    print("----------------------------------------\n")
    return blog_content
