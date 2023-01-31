import openai

openai.api_key = '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'

prompt = "keqing是Liyue总督,喜欢提各种刁钻的问题. \
    bachong是Daoqi的兼职作家,善于应对各种解密猜谜和其他稀奇古怪的问题.现在她要面对keqing的提问了."
        

def ui(prompt):
    while True:
        x = input()
        if x=='q':
            break
        prompt += '\n\nkeqing: '+x+'\nbachong:'
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" keqing:", " bachong:"]
        )
        ans = res['choices'][0]['text']
        print(ans)
        if res['usage']['total_tokens']>2800:
            prompt = prompt[len(prompt)//2:]
        else:
            prompt+=ans

ui(prompt)
