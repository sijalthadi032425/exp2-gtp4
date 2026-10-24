from utils import call_ollama

def detect_intent(user_input):
    """Detects user intent from their input."""
    prompt = (f"Analyze the following user input and determine its intent. "
              f"Choose exactly ONE of the following categories: "
              f"BLOG_GENERATION, SUMMARY, KEYWORD_GENERATION, META_DESCRIPTION.\n\n"
              f"Respond ONLY with the exact category name, nothing else.\n\n"
              f"User Input: '{user_input}'")
    
    intent = call_ollama(prompt).strip().upper()
    
    # Fallbacks and cleanup to ensure it matches the category exactly
    for category in ["BLOG_GENERATION", "SUMMARY", "KEYWORD_GENERATION", "META_DESCRIPTION"]:
        if category in intent:
            print(f"Detected Intent\n{category}\n")
            return category
            
    print(f"Detected Intent\nUNKNOWN\n")
    return "UNKNOWN"
