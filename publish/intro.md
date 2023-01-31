
chat with GPT-3 with 引导剧本  
created at 2022-12-31

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt0 = "keqing和bachong开始了一场冒险，从阿莱斯加巨大雨林开始. \
    前方充满了未知，不知道会有什么样的生物，什么样的奇观，什么样的意外在等着她们呢？\
        \n\nkeqing: 前面有一个好大的山洞，会不会藏有什么宝藏，bachong我们快去看看\
        \nbachong: 好啊好啊，我们一起去看看。啊，洞里好黑啊，什么都看不见，你带了什么照明工具吗？\
        \n\nkeqing: 幸好我的LED灯还有些电量，还能坚持几个小时。哇，那乱七八糟的一堆是什么？啊啊啊，是骨头！是骨头！\
        \nbachong: keqing别怕，只是过去的探险者留下的尸骸，我们这么聪明，不会重蹈他们的覆辙的。只不过，接下来，看起来要小心了。"


def ui(prompt0):
    prompt = prompt0
    while True:
        x = input()
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
            prompt = prompt0
        else:
            prompt+=ans

ui(prompt0)
```