import os
from openai import AzureOpenAI
from typing import List
import rich
from pydantic import BaseModel

# https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
endpoint = os.getenv("ENDPOINT_URL", "https://azaifoundrydemo.cognitiveservices.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "DkVMEyGKw4eIQY6uzcjagqfi4i74AD5Bf2GmoeLRf0PT8hEFWTi9JQQJ99BJACYeBjFXJ3w3AAAAACOGKEXr")
api_version = "2023-07-01-preview"

class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Create a completion (the SDK exposes `create` on chat completions)
completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "solve 8x + 31 = 2"},
    ],
    max_tokens=500,
)

# The SDK returns choices with message content. We'll attempt to parse the assistant
# text as JSON matching our MathResponse model. If parsing fails, print the raw text.
message = completion.choices[0].message
assistant_text = None
if isinstance(message, dict):
    # Some SDK versions return a mapping-like message
    assistant_text = message.get("content") or message.get("content", "")
else:
    # Try attribute access
    assistant_text = getattr(message, "content", None) or getattr(message, "text", None)

if not assistant_text:
    # Fallback: try top-level text on the choice
    assistant_text = getattr(completion.choices[0], "text", None)

import json
from pydantic import ValidationError

try:
    parsed = MathResponse.model_validate(json.loads(assistant_text))
    rich.print(parsed.steps)
    print("answer:", parsed.final_answer)
except (json.JSONDecodeError, ValidationError, TypeError) as e:
    print("Could not parse assistant output as MathResponse model:", e)
    print("Raw assistant output:\n", assistant_text)

