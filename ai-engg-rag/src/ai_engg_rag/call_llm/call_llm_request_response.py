import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

#load the environment vaiables
load_dotenv()

class ChatService:
    #Constructor
    def __init__(self):
        api_key = os.environ["OPENROUTER_API_KEY"]
        base_url = os.environ["OPENROUTER_BASE_URL"]

        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )

    async def ask(self, question: str) -> str:
        response = await self.client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b:free", #mention the model you want to use
            messages=[
                {
                    "role":"user",
                    "content": question
                }
            ]
        )

        if not response.choices:
            raise ValueError(f"Empty choices in response. Full response: {response}")

        return response.choices[0].message.content

async def main():
    chat_service = ChatService()
    query = input("Query:") #method used to take user input
    answer = await chat_service.ask(query)
    print(answer)

if __name__ == "__main__":
    asyncio.run(main())