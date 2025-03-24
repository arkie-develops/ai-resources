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

def generate_api_endpoint(
    endpoint_name,
    method,
    request_params,
    response_structure,
    security_requirements
):
    generation_prompt = f"""
    Generate a complete API endpoint implementation with the following specifications:

    Endpoint: {endpoint_name}
    HTTP Method: {method}
    Request Parameters: {request_params}
    Expected Response Structure: {response_structure}
    Security Requirements: {security_requirements}

    Please provide:
    1. Complete implementation code
    2. Input validation
    3. Error handling for all edge cases
    4. Security middleware implementation
    5. Documentation including:
       - OpenAPI/Swagger specification
       - Example requests and responses
       - Rate limiting considerations
       - Caching strategy
    """
    return send_prompt(generation_prompt)

# Example usage: Generating a user authentication endpoint
endpoint_spec = generate_api_endpoint(
    endpoint_name="/api/v1/auth/login",
    method="POST",
    request_params={
        "email": "string, required, valid email format",
        "password": "string, required, min 8 characters",
        "remember_me": "boolean, optional"
    },
    response_structure={
        "access_token": "string",
        "refresh_token": "string",
        "expires_in": "number"
    },
    security_requirements=["rate limiting", "CORS", "input sanitization"]
)

print(endpoint_spec)
