from openai import OpenAI

def send_prompt(prompt):
    """
    Sends a prompt to the OpenAI API and returns the response.

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

def analyze_code_complexity(function_code):
    analysis_prompt = f"""
    Perform a comprehensive complexity analysis of this function:

    {function_code}

    Provide analysis of:
    1. Time Complexity (Big O notation with explanation)
    2. Space Complexity (Big O notation with explanation)
    3. Cognitive Complexity (how difficult the code is to understand)
    4. Cyclomatic Complexity (number of linear paths through the code)

    For each metric, explain:
    - Why you arrived at that assessment
    - Potential optimization opportunities
    - Trade-offs of any suggested improvements
    """

    return send_prompt(analysis_prompt)

# Example usage for a sorting function
code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

analysis = analyze_code_complexity(code)