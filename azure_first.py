import os
from openai import AzureOpenAI

# may change in the future

# https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
endpoint = os.getenv("ENDPOINT_URL", "https://azaifoundrydemo.cognitiveservices.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "DkVMEyGKw4eIQY6uzcjagqfi4i74AD5Bf2GmoeLRf0PT8hEFWTi9JQQJ99BJACYeBjFXJ3w3AAAAACOGKEXr")
api_version = "2025-01-01-preview"

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

completion = client.chat.completions.create(
    model= deployment,  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "Hello, tell me a tech joke.",
        },
    ],
)
print(completion.to_json())

# Print only the assistant (AI) generated message content
message = completion.choices[0].message
assistant_text = None
if isinstance(message, dict):
    assistant_text = message.get("content") or message.get("text")
else:
    assistant_text = getattr(message, "content", None) or getattr(message, "text", None)

if not assistant_text:
    # fallback to top-level choice text
    assistant_text = getattr(completion.choices[0], "text", None) or getattr(completion, "text", None)

print(assistant_text)

