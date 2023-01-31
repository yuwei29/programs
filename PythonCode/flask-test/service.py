class Service:
  def __init__(self):
    self.a = 'abcde'
    self.中 = '中文内容'
    
  def changeCn(self,content):
    self.中 = content
    
  def getLen(self):
    return len(self.a)+len(self.中)