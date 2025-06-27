# Tool-Enhanced Reasoning System

This project implements a tool-enhanced reasoning system that uses Google's Gemini model to solve various queries by leveraging specialized tools for mathematical and string operations.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd W3D2_q3_tool_enhanced_reasoning
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Get an API key from Google AI Studio
   - Replace the placeholder in `main.py` with your actual API key

## Usage

Run the script with:

```bash
python main.py
```

Then enter your query when prompted.

## Available Tools

1. **Mathematical Tools**

   - `average(numbers)`: Calculates the average of a list of numbers
   - `square_root(number)`: Calculates the square root of a number

2. **String Tools**
   - `count_vowels(word)`: Counts the number of vowels in a word
   - `count_letters(word)`: Counts the number of letters in a word

## Example Queries and Outputs

### Test Query 1:

**Input:** What is the average of the numbers 5, 7, and 9?

**Output:**

```
The average of 5, 7, and 9 is 7.0
```

### Test Query 2:

**Input:** Calculate the square root of 64.

**Output:**

```
The square root of 64 is 8.0
```

### Test Query 3:

**Input:** Count the vowels in the word "banana".

**Output:**

```
The word "banana" contains 3 vowels
```

### Test Query 4:

**Input:** How many letters are in the word "elephant"?

**Output:**

```
The word "elephant" has 8 letters
```

### Test Query 5:

**Input:** Find the average of 10, 20, and 30, and then calculate the square root of the result.

**Output:**

```
The average of 10, 20, and 30 is 20.0
The square root of 20.0 is approximately 4.472
```

## Tool Usage Decision Making

The system uses a prompt-based approach to determine when to use tools:

1. The Gemini model analyzes the query and identifies which operations are needed
2. When a tool is needed, the model formats the tool call in the format: `TOOL: function_name(arguments)`
3. The system extracts and executes the tool call
4. The result is incorporated into the final response

Tools are selected based on the nature of the operation:

- Math operations (averages, square roots) use the math tools
- Text analysis (counting letters, vowels) uses the string tools
- Complex queries may chain multiple tool calls together

The system is designed to be extensible - new tools can be added by:

1. Creating the tool function in the appropriate module
2. Adding it to the `TOOL_FUNCTIONS` dictionary in `main.py`
3. Updating the prompt to document the new tool's usage
