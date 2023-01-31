actions = ['left','middle','right']
judge = lambda x:0 if x=='middle' else 1 if x=='right' else -1

class Player:
    def __init__(self):
        self.totry = 0
        self.best = None
        self.highScore = float('-inf')
    
    def policy(self):
        if self.totry>2:
            return actions[self.best]
        else:
            return actions[self.totry]

    def update(self,reward):
        if reward > self.highScore:
            self.best = self.totry
            self.highScore = reward
        self.totry+=1

# 对 action链长度>=2 也适用，view 整个action链 as an action 即可 
# 最朴素的策略就是 穷举 所有可能操作，再选 符合需求的 
p = Player()
for i in range(10):
    action = p.policy()
    reward = judge(action)
    p.update(reward)
    print(action,reward)