def f(x):
  a=[0,1,2,3,5]
  e=5
  for i in range(5):
    try:
      f=e/a[i]
      print(f)
    except:
      pass
    print("loop at "+str(i))
  print(x)

f(13)
