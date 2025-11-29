
class my_number:
  def __init__(self, number: int):
    self.number = number
    
  def print(self):
    print(self.number)
    
    
  def invert(self):
    number_str = str(number)
    number_len = len(self.number)
    inverted = ""
    for i in range(number_len):
      char = number_str[number_len-i-1]
      inverted += char
      print(inverted)

number = my_number(345)