#!/usr/bin/env python
import os
from openai import AzureOpenAI

# https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
endpoint = os.getenv("ENDPOINT_URL", "https://azaifoundrydemo.cognitiveservices.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2025-01-01-preview")
deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "DkVMEyGKw4eIQY6uzcjagqfi4i74AD5Bf2GmoeLRf0PT8hEFWTi9JQQJ99BJACYeBjFXJ3w3AAAAACOGKEXr")
api_version = "2023-07-01-preview"

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

prompt = "A tucan bird lounging in a tropical resort in space, pixel art"
model = "dall-e-3"


def main() -> None:
    # Generate an image based on the prompt
    response = client.images.generate(prompt=prompt, model=model)

    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()