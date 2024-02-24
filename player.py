from stats import Stats

"""
Player Class:
  Variables:
    1. Team Comp
    2. Cards in hand
    3. Health
    4. Energy
    5. Guard
    6. Mora
    7. Upgradable Card Pile
    8. Draw pile
    9. Discard Pile
   10. Action Points
   11. Attack
"""

class Player(Stats):
  def __init__(self):
    super().__init__()
    ap = 0
    team = []
    cardsInHand = []
    cardShop = []
    drawPile = []
    discardPile = []
    

  
  def getAP(self):
    return self.ap
  
  def getTeam(self):
    return self.team
  
  def getCardsInHand(self):
    return self.cardsInHand

  def getCardShop(self):
    return self.cardShop

  def getDrawPile(self):
    return self.drawPile
  
  def getDiscardPile(self):
    return self.discardPile

  def setAP(self, AP):
    self.ap = AP

  def increaseAP(self, plus):
    #have to check if there is a cap on AP
    pass

  def decreaseAP(self, minus):
    newAP = self.ap - minus
    if newAP > 0:
      self.ap = newAP
    else:
      self.ap = 0

  def setTeam(self, c1, c2, c3, c4):
    self.team.append(c1)
    self.team.append(c2)
    self.team.append(c3)
    self.team.append(c4)

  def playCard(self, card):
    if card in self.getCardsInHand:
      #execute card 
      #use up repective AP
      #remove card from hand and put in discard
      #add card to discard unless specified to trash
      pass
    else:
      #prompt user that card is not in hand
      pass
  
  def displayShop(self):
    pass

  def buyCard(self):
    #use displayShop to view the shop contents
    pass

  def draw(self):
    #draw 0th index from drawpile
    #remove form drawpile
    #add to hand
    pass

  def shuffle(self):
    #shuffle discard deck and add to bottom of draw pile
    pass

if __name__ == '__main__':
  a= Player()
  a.setHealth(10)
  print(a.getHealth())