from openai import OpenAI
'''
Update the following code with your API key.

You need to create your own account to get your own API key to ensure you don’t have to wait for others by going to: OpenRouter https://openrouter.ai

Once you have signed up, go to: https://openrouter.ai/settings/keys to create your API key
'''
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


def get_code_summary(code_snippet, focus_area="functionality"):
    """
    Generates a summary for the given code snippet based on the focus area.

    Args:
        code_snippet (str): The code to be analyzed.
        focus_area (str): The focus area for the summary (e.g., functionality, security).

    Returns:
        str: A concise summary of the code.
    """
    summary_prompt = f"""
    Analyze this code and provide a concise summary focusing on {focus_area}:

    {code_snippet}

    Include in your summary:
    1. Main purpose of the code
    2. Key functions and their roles
    3. Important dependencies or assumptions
    4. Potential areas of concern

    Format the response as a clear, paragraph-based summary.
    """

    return send_prompt(summary_prompt)

# Usage example
code = """
def process_user_data(user_id, data):
    if not validate_user(user_id):
        raise ValueError("Invalid user")

    processed = transform_data(data)
    store_in_cache(user_id, processed)
    notify_processors(user_id)
    return processed
"""

summary = get_code_summary(code, focus_area="data flow and security")
print(summary)