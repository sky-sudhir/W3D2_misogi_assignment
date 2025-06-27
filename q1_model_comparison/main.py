import os
from providers.gemini_api import run_gemini
from providers.ollama_runner import run_ollama
from dotenv import load_dotenv

load_dotenv()

# OLLAMA_MODEL = 'phi3:3.8b'  # Change as needed
OLLAMA_MODEL = 'qwen2.5:3b'  # Change as needed

def choose_model():
    print("\n🤖 Choose model:")
    print("[1] Gemini")
    print(f"[2] Ollama ({OLLAMA_MODEL})")
    while True:
        choice = input("\nYour choice: ").strip()
        if choice in ['1', '2']:
            return choice
        print("❌ Invalid input. Choose 1 or 2.")

def log_output(prompt, model, output, filepath='comparisons.md'):
    with open(filepath, 'a') as f:
        f.write(f"## Prompt: {prompt}\n")
        f.write(f"**Model:** {model}\n")
        f.write("```\n")
        f.write(output.strip() + "\n```\n\n")

def main_loop():
    print("🚀 Model Comparison CLI Tool")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("📝 Enter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == 'exit':
            break

        model_choice = choose_model()

        if model_choice == '1':
            output = run_gemini(prompt)
            print("\n📤 Gemini Output:")
            log_output(prompt, "Gemini", output)
        else:
            output = run_ollama(OLLAMA_MODEL, prompt)
            print(f"\n📤 Ollama ({OLLAMA_MODEL}) Output:")
            log_output(prompt, f"Ollama ({OLLAMA_MODEL})", output)

        print(output)
        print("\n" + "-"*50 + "\n")

if __name__ == '__main__':
    main_loop()
