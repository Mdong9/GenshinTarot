#Base Genshin game goes here
import random

"""
Character Class:
  Variables:
    1. Name
    2. Ultimate
    3. Normal Cards
    4. Unupgraded Cards

Card Class:
  Draw Function
  Discard Function
  Variables:
    For character cards:
      1. Name
      2. Description
      3. Action point cost
      4. type (upgraded or not)
    For Effect Cards:
      1. Name
      2. Description
      3. Effect
"""
class Card():
  def __init__(self, c):
    name = ""
    #description/ability?
    cost = 0

  def setName(self, Name):
    self.name = Name
  
  def setCost(self, Cost):
    self.cost = Cost

  def getName(self):
    return self.name
  
  def getCost(self):
    return self.cost
  
class Character():
  '''
  1. name
  2. their cards
  3. their ultimate
  '''
  pass




if __name__ == '__main__':

  # print(x.getName())
  # print(x.getHealth())
  # x.decreaseHealth(13)
  # print(x.getHealth())