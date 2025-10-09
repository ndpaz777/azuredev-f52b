import os
from openai import AzureOpenAI

# may change in the future

# https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
endpoint = os.getenv("ENDPOINT_URL", "https://azaifoundrydemo.cognitiveservices.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "DkVMEyGKw4eIQY6uzcjagqfi4i74AD5Bf2GmoeLRf0PT8hEFWTi9JQQJ99BJACYeBjFXJ3w3AAAAACOGKEXr")
api_version = "2023-07-01-preview"

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
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())

