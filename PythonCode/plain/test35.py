import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt0 = "The following is a conversation with an AI assistant. \
    The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\
        \nAI: I am an AI created by OpenAI. How can I help you today?"


def ui(prompt0):
    prompt = prompt0
    while True:
        x = input()
        prompt += '\n\nHuman: '+x+'\nAI:'
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        ans = res['choices'][0]['text']
        print(ans)
        if res['usage']['total_tokens']>2800:
            prompt = prompt0
        else:
            prompt+=ans

ui(prompt0)
