from .sub import mod1
from .sub import mod2
def f(x):
  return mod1.f(x)+mod2.f(x)
def g(x):
  return mod1.f(x+2)