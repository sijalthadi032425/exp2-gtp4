import ollama
import os

def call_ollama(prompt, model="llama3.2"):
    """Helper function to call Ollama model and return the response text."""
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response.get("response", "").strip()
    except Exception as e:
        return f"Error communicating with Ollama. Make sure Ollama is running and the model '{model}' is pulled. Details: {e}"

def save_to_file(content, filename="outputs/generated_blog.txt"):
    """Saves generated content to a text file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n" + "-"*50 + "\n\n")
    print(f"Content successfully saved to {filename}")
