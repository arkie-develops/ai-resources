from openai import OpenAI

def send_prompt(prompt):
    """
    Sends a prompt to the openrouter API and returns the response.

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
def transform_code(code, source_lang, target_lang, maintain_features=None):
    if maintain_features is None:
        maintain_features = ["functionality", "error handling", "routing"]

    transform_prompt = f"""
    Transform this {source_lang} code into equivalent {target_lang} code:

    Original {source_lang} code:
    {code}

    Requirements:
    1. Maintain these specific features: {', '.join(maintain_features)}
    2. Follow {target_lang} best practices and idioms
    3. Preserve all error handling and edge cases
    4. Add comments explaining any significant changes
    5. Include any necessary imports or dependencies

    Provide the transformed code with:
    - Implementation notes
    - Any necessary setup instructions
    - Warnings about potential compatibility issues
    """

    return send_prompt(transform_prompt)

# Example usage: Converting a Python Flask server to a Node.js (Express) server
flask_code = """
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    if not data:
        return jsonify(error="No data provided"), 400
    processed_data = {key: value.upper() for key, value in data.items()}
    return jsonify(processed_data=processed_data)

if __name__ == '__main__':
    app.run(debug=True)
"""

js_version = transform_code(
    flask_code,
    "Python (Flask)",
    "JavaScript (Node.js/Express)",
    ["routing", "error handling", "JSON handling"]
)

print(js_version)