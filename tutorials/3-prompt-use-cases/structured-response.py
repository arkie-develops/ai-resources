from openai import OpenAI

def send_prompt(prompt):
    """
    Sends a prompt to the Openrouter API and returns the response.

    Args:
        prompt (str): The text prompt to send to the model.

    Returns:
        str: The content of the model's response.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPENROUTER_API_KEY>",
    )

    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.1-70b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

import json

def analyze_code_quality(code_snippet):
    analysis_prompt = f"""
    Analyze this code and provide only a JSON response with the following structure:
    {{
        "quality_metrics": {{
            "maintainability_index": "number between 0-100",
            "cyclomatic_complexity": "number",
            "cognitive_complexity": "number"
        }},
        "issues": [
            {{
                "type": "string",
                "severity": "high" | "medium" | "low",
                "description": "string",
                "line_number": "number",
                "suggested_fix": "string"
            }}
        ],
        "refactoring_needed": "boolean",
        "estimated_technical_debt_hours": "number"
    }}

    Code to analyse:
    {code_snippet}

    Do not provide any explanations, just the json object
    """

    response = send_prompt(analysis_prompt)

    response_json = response.replace('\\n', '').strip()
    response_json = response_json.replace('```json', '').strip()
    response_json = response_json.replace('```', '').strip()

    #Strip hidden utf strings from API response
    clean_string = response_json.strip().replace('\ufeff', '')
    try:
      response_json = json.loads(clean_string)
      print("JSON is valid!")
    except json.JSONDecodeError as e:
      print("Invalid JSON:", e)

    return response_json

example_code = """
def calculate_factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
"""

# Assuming `send_prompt` and `analyze_code_quality` are defined
analysis_result = analyze_code_quality(example_code)

print(json.dumps(analysis_result, indent=4))

# Accessing fields from the JSON object
if analysis_result:
    # Access quality metrics
    maintainability_index = analysis_result["quality_metrics"]["maintainability_index"]
    cyclomatic_complexity = analysis_result["quality_metrics"]["cyclomatic_complexity"]
    cognitive_complexity = analysis_result["quality_metrics"]["cognitive_complexity"]

    print(f"Maintainability Index: {maintainability_index}")
    print(f"Cyclomatic Complexity: {cyclomatic_complexity}")
    print(f"Cognitive Complexity: {cognitive_complexity}")

    # Access and iterate through issues
    issues = analysis_result.get("issues", [])
    for issue in issues:
        print(f"Issue Type: {issue['type']}, Severity: {issue['severity']}")
        print(f"Description: {issue['description']}")
        print(f"Line Number: {issue['line_number']}")
        print(f"Suggested Fix: {issue['suggested_fix']}")

    # Access refactoring suggestion
    refactoring_needed = analysis_result["refactoring_needed"]
    print(f"Refactoring Needed: {refactoring_needed}")

    # Access estimated technical debt hours
    technical_debt_hours = analysis_result["estimated_technical_debt_hours"]
    print(f"Estimated Technical Debt Hours: {technical_debt_hours}")