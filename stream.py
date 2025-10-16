import os
import asyncio

from openai import AzureOpenAI, AsyncAzureOpenAI

# may change in the future

# https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
# The Azure endpoint should be the base resource host (no path/query).
# Example: https://my-resource-name.openai.azure.com
endpoint = os.getenv("ENDPOINT_URL", "https://azaifoundrydemo.cognitiveservices.azure.com")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "DkVMEyGKw4eIQY6uzcjagqfi4i74AD5Bf2GmoeLRf0PT8hEFWTi9JQQJ99BJACYeBjFXJ3w3AAAAACOGKEXr")
api_version = "2025-01-01-preview"

# ==================================================================

def sync_main() -> None:
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )
    # For chat-capable models (gpt-*) use the chat completions API and supply
    # a messages list instead of a simple prompt string. Using the wrong
    # endpoint or data type can trigger 'Unsupported data type'.
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": "A,B,C,"}],
        max_tokens=5,
        temperature=0,
        stream=True,
    )

    # You can manually control iteration over the response
    first = next(response)
    print(f"got response data: {first.to_json()}")

    # Or you could automatically iterate through all of data.
    # Note that the for loop will not exit until *all* of the data has been processed.
    for data in response:
        print(data.to_json())


async def async_main() -> None:
    client = AsyncAzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )
    response = await client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": "A,B,C,"}],
        max_tokens=5,
        temperature=0,
        stream=True,
    )

    # You can manually control iteration over the response.
    # In Python 3.10+ you can also use the `await anext(response)` builtin instead
    first = await response.__anext__()
    print(f"got response data: {first.to_json()}")

    # Or you could automatically iterate through all of data.
    # Note that the for loop will not exit until *all* of the data has been processed.
    async for data in response:
        print(data.to_json())


sync_main()

asyncio.run(async_main())
