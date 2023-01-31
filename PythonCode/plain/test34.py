import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt0 = "GPT是一个非常聪明的问答机器人,如果问它具有明确清晰答案的问题, 它会给出准确的回答。\
    如果所问的问题含义不明, 或者没有确定的答案, 它也能给出巧妙的回答.\
    \n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\
    \n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\
    \n\nQ: What is the square root of banana?\nA: sqrt(banana)\
    \n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\
    \n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\
    \n\nQ: Where is the Valley of Kings?\nA: The Valley of Kings is located in Luxor, Egypt.\
    \n\nQ: 美国建国时间是？\nA: 美国建国时间是1776年7月4日。\n\nQ: 长江和黄河哪个长？\nA: 长江比黄河长。\
    \n\nQ: 第一个进入太空的人是谁？\nA: 第一个进入太空的人是尤里·阿列克谢耶维奇·加加林。\
    \n\nQ: 打雷的时候关窗户有用吗？\nA: 没用，我关上窗子后，还在一直打雷。\
    \n\nQ: Which superpower is better: the ability to talk to ducks or to have the best parking space wherever you went? Why?\
    \nA: That depends on the individual. The ability to talk to ducks could be a great way to learn more about the natural world, \
    while the best parking space could be a great convenience. \
    Ultimately, it is up to the individual to decide which superpower is better for them."

def ui(prompt0):
  prompt = prompt0
  while True:
    x = input()
    prompt += ('\n\nQ: '+x+'\nA:')
    res = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=1200,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["\n"]
    )
    ans = res['choices'][0]['text']
    print(ans)
    if res['usage']['total_tokens']>2800:
      prompt = prompt0
    else:
      prompt+=ans

ui(prompt0)
