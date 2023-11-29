from openai import AsyncOpenAI

from src.python.domain.message.Message import Message


class GPTClient:
    def __init__(self, environment):
        self.environment = environment
        self.client = AsyncOpenAI(api_key=self.environment.openAIApiKey)

    async def getResponse(self, conversationHistory, question, model="gpt-4-1106-preview"):
        messages = [{"role": "system", "content": self.environment.gptSystem}]
        messages.extend(conversationHistory)  # Add the entire conversation history
        messages.append({"role": "user", "content": question})
        try:
            stream = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                max_tokens=500
            )
            response = ""

            async for part in stream:
                response += part.choices[0].delta.content or ""

            return response
        except Exception as e:
            print(f"Error while querying OpenAI: {e}")
            return Message.GTPSorry
