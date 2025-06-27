import os
import google.generativeai as genai
import ast
from tools.math_tools import average, square_root
from tools.string_tools import count_vowels, count_letters

# Load Gemini
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")

# Available tools mapping
TOOL_FUNCTIONS = {
    "average": average,
    "square_root": square_root,
    "count_vowels": count_vowels,
    "count_letters": count_letters
}

def ask_gemini(query):
    prompt = f"""You are a helpful assistant that reasons step-by-step (Chain of Thought, CoT) to solve queries.

When you need to use a tool, state clearly which tool you would use and what arguments you would pass. For example:

TOOL: average([1, **TOOL:** square_root(25) **TOOL:**count_vowels("hello") **TOOL:**count_letters("world")`

After stating the tool, continue your reasoning and provide a final answer.

Available Tools:

average(numbers: list): Calculates the average of a list of numbers.

square_root(number): Calculates the square root of a number.

count_vowels(word): Counts the number of vowels in a word.

count_letters(word): Counts the number of letters in a word.

Query: {query}
Reasoning:
(You will provide step-by-step reasoning here)"""
    response = model.generate_content(prompt)
    return response.text

def extract_tool_call(text):
    if "TOOL:" in text:
        tool_line = [line for line in text.splitlines() if line.startswith("TOOL:")][0]
        tool_call = tool_line.replace("TOOL:", "").strip()
        tool_name = tool_call.split("(")[0]
        args_str = tool_call.split("(")[1].rstrip(")")
        
        # Try parsing args safely using ast
        try:
            args = ast.literal_eval(args_str)
        except Exception:
            # Fallback: wrap unquoted word with quotes
            if not args_str.startswith(("'", '"', "[")):
                args = args_str.strip()
                args = f'"{args}"'  # wrap in quotes
                args = ast.literal_eval(args)
        return tool_name, args
    return None, None
def main():
    query = input("Enter your query: ")
    reasoning = ask_gemini(query)
    print("\n--- Reasoning from Gemini ---")
    print(reasoning)

    tool_name, args = extract_tool_call(reasoning)
    if tool_name:
        func = TOOL_FUNCTIONS.get(tool_name)
        if func:
            result = func(args)
            print(f"\n🛠️ Tool Used: {tool_name}({args}) = {result}")
        else:
            print("\n⚠️ Tool not found.")
    else:
        print("\nℹ️ No tool used.")

if __name__ == "__main__":
    main()
