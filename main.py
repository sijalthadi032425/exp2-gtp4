import os
import sys
from input_module import get_user_inputs
from blog_module import generate_blog
from title_module import generate_titles
from summary_module import generate_summary
from keyword_module import generate_keywords
from meta_module import generate_meta_description
from intent_module import detect_intent
from utils import save_to_file

def main():
    print("="*50)
    print("AI-Powered Blog Content Generator using Ollama")
    print("="*50)
    
    current_blog = None
    
    while True:
        print("\n" + "="*30)
        print("Main Menu")
        print("="*30)
        print("1. Standard Workflow (Generate Blog & Elements)")
        print("2. Intent Detection Mode (Natural Language)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            inputs = get_user_inputs()
            current_blog = generate_blog(inputs)
            save_to_file(f"--- Blog: {inputs['topic']} ---\n{current_blog}")
            
            while True:
                print("\n" + "-"*30)
                print("Blog Operations Menu")
                print("-"*30)
                print("1. Generate Titles")
                print("2. Generate Summary")
                print("3. Generate SEO Keywords")
                print("4. Generate Meta Description")
                print("5. Return to Main Menu")
                
                op_choice = input("\nEnter operation (1-5): ")
                
                if op_choice == "1":
                    titles = generate_titles(current_blog)
                    save_to_file(f"--- Titles ---\n{titles}")
                elif op_choice == "2":
                    summary = generate_summary(current_blog)
                    save_to_file(f"--- Summary ---\n{summary}")
                elif op_choice == "3":
                    keywords = generate_keywords(current_blog)
                    save_to_file(f"--- SEO Keywords ---\n{keywords}")
                elif op_choice == "4":
                    meta = generate_meta_description(current_blog)
                    save_to_file(f"--- Meta Description ---\n{meta}")
                elif op_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
        elif choice == "2":
            print("\nIntent Detection Mode")
            user_query = input("User\n")
            intent = detect_intent(user_query)
            
            if intent == "BLOG_GENERATION":
                print("Proceeding to generate a blog...")
                inputs = get_user_inputs()
                current_blog = generate_blog(inputs)
                save_to_file(f"--- Blog: {inputs['topic']} ---\n{current_blog}")
            elif intent == "SUMMARY":
                if not current_blog:
                    print("Error: No blog generated yet. Please generate a blog first.")
                else:
                    summary = generate_summary(current_blog)
                    save_to_file(f"--- Summary ---\n{summary}")
            elif intent == "KEYWORD_GENERATION":
                if not current_blog:
                    print("Error: No blog generated yet. Please generate a blog first.")
                else:
                    keywords = generate_keywords(current_blog)
                    save_to_file(f"--- SEO Keywords ---\n{keywords}")
            elif intent == "META_DESCRIPTION":
                if not current_blog:
                    print("Error: No blog generated yet. Please generate a blog first.")
                else:
                    meta = generate_meta_description(current_blog)
                    save_to_file(f"--- Meta Description ---\n{meta}")
            else:
                print(f"Could not fulfill request for intent: {intent}")
                
        elif choice == "3":
            print("\nExiting the application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    main()
