def get_user_inputs():
    """Prompts the user for details about the blog to be generated."""
    print("Enter Blog Details:")
    topic = input("Enter Blog Topic: ")
    style = input("Writing Style (e.g., Professional, Casual): ")
    tone = input("Tone (e.g., Formal, Friendly): ")
    word_count = input("Word Count (e.g., 500): ")
    
    print("\n----------------------------------")
    print(f"Blog Topic : {topic}")
    print(f"Style      : {style}")
    print(f"Tone       : {tone}")
    print(f"Words      : {word_count}")
    print("----------------------------------\n")
    
    return {
        "topic": topic,
        "style": style,
        "tone": tone,
        "word_count": word_count
    }
