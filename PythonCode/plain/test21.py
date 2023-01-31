m,s,t = map(int,input().split())
''' 守望者的跑步速度为 17m/s，以这样的速度是无法逃离荒岛的。庆幸的是守望者拥有闪烁法术，可在 1s 内移动 60m，
不过每次使用闪烁法术都会消耗魔法值 10 点。守望者的魔法值恢复的速度为 4 点每秒，只有处在原地休息状态时才能恢复。

现在已知守望者的魔法初值 M，他所在的初始位置与岛的出口之间的距离 S，岛沉没的时间 T。
你的任务是写一个程序帮助守望者计算如何在最短的时间内逃离荒岛，若不能逃出，则输出守望者在剩下的时间内能走的最远距离。

注意：守望者跑步、闪烁或休息活动均以秒为单位，且每次活动的持续时间为整数秒。距离的单位为米。'''

# 1 chongyu  60m/s
# 2 jinji   17m/s
# 3  3.5s  60m      60/3.5 =  120/7 = 17.1...
if m>=10*( s//60+(s%60!=0) ):
    d = 60*t
    tmin = s//60+(s%60!=0)
    if tmin<=t:
        print("Yes")
        print(tmin)
    else:
        print("No")
        print(d)
elif m+4*t<=10:
    d=17*t
    tmin = s//17+(s%17!=0)
    if tmin<=t:
        print("Yes")
        print(tmin)
    else:
        print("No")
        print(d)
elif m>=10*t:
    print("No")
    print(60*t)
else: 
    #用掉能用的m，跑不出去，且尚未超时
    tmin = m//10
    d = tmin*60
    t -= tmin # t>0
    s -= d #s>0
    m %= 10
    
    print("No")
    print(17*t)