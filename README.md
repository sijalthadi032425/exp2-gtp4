# AI-Powered Blog Content Generator

This project is a modular AI-powered Blog Content Generator built using Python and Ollama. It corresponds to **Experiment 2** for your coursework.

## Features
- Generates high-quality blogs based on user inputs (Topic, Style, Tone, Word count).
- Suggests 5 attractive titles for the generated blog.
- Generates a short summary of the blog.
- Extracts SEO-friendly keywords.
- Creates an SEO meta description (under 160 characters).
- Includes an Intelligent Intent Detection module that routes natural language prompts using Ollama.

## Project Structure
- `main.py`: The entry point for the application, featuring a continuous menu-driven interface.
- `input_module.py`: Handles user data collection.
- `blog_module.py`: Core blog generation logic.
- `title_module.py`, `summary_module.py`, `keyword_module.py`, `meta_module.py`: Post-generation processing modules.
- `intent_module.py`: LLM-based intent detector.
- `utils.py`: Helper functions, including the Ollama integration layer and file saving functionality.
- `outputs/`: Folder where all text outputs are automatically saved.

## Setup Instructions

1. **Install Ollama**:
   Make sure you have [Ollama](https://ollama.com/) installed on your machine and running in the background.
   
2. **Pull the Llama 3.2 Model**:
   Open a terminal and run:
   ```bash
   ollama run llama3.2
   ```

3. **Install Python Dependencies**:
   Open a terminal in this directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Execute the main script:
   ```bash
   python main.py
   ```
