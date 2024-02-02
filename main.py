#Base Genshin game goes here
import random

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

Enemy Class:
  Variables:
    1. Type (Normal, Elite, Boss)
    2. Mora
    3. Health
    4. Guard
    5. Attack

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

Board State Class:
  1. Clock Turn
  2. Leyline modifiers
  3. Player Phase -> Enemy Phase
"""

class Stats:
  def __init__(self):
    name = ""
    health = 0
    energy = 0
    guard = 0
    mora = 0
    attack = 0
  
  def getName(self):
    return self.name

  def getHealth(self):
    return self.health

  def getEnergy(self):
    return self.energy

  def getGuard(self):
    return self.guard

  def getMora(self):
    return self.mora

  def getAttack(self):
    return self.attack
  
  def setName(self, NAME):
    self.name = NAME
  
  def setHealth(self, HEALTH):
    self.health = HEALTH

  def setEnergy(self, ENERGY):
    self.energy = ENERGY

  def setGuard(self, GUARD):
    self.guard = GUARD

  def setMora(self, MORA):
    self.mora = MORA
  
  def setAttack(self, ATTACK):
    self.attack = ATTACK

  def setStats(self, NAME: str, HEALTH: int, ENERGY: int, GUARD: int, MORA: int, ATTACK: int):
    self.setName(NAME)
    self.setHealth(HEALTH)
    self.setEnergy(ENERGY)
    self.setGuard(GUARD)
    self.setMora(MORA)
    self.setAttack(ATTACK)

  def increaseHealth(self, plus):
    newHealth = self.health + plus
    if newHealth < 12:
      self.health = newHealth
    else:
      self.health = 12
  
  def decreaseHealth(self, minus):
    newHealth = self.health - minus
    if newHealth > 0:
      self.health = newHealth
    else:
      self.health = 0

  def increaseEnergy(self, plus):
    newEnergy = self.energy + plus
    if newEnergy < 12:
      self.energy = newEnergy
    else:
      self.energy = 12
  
  def decreaseEnergy(self, minus):
    newEnergy = self.energy - minus
    if newEnergy > 0:
      self.energy = newEnergy
    else:
      self.energy = 0

  def increaseGuard(self, plus):
    newGuard = self.guard + plus
    if newGuard < 12:
      self.guard = newGuard
    else:
      self.guard = 12

  def decreaseGuard(self, minus):
    newGuard = self.guard - minus
    if newGuard > 0:
      self.guard = newGuard
    else:
      self.guard = 0

  def increaseMora(self, plus):
    newMora = self.mora + plus
    if newMora < 12:
      self.mora = newMora
    else:
      self.mora = 12

  def decreaseMora(self, minus):
    newMora = self.mora - minus
    if newMora > 0:
      self.mora = newMora
    else:
      self.mora = 0

  def increaseAttack(self, plus):
    self.attack = self.attack + plus
  
  def decreaseAttack(self, minus):
    self.attack = self.attack - minus

class Player(Stats):
  def __init__(self):
    ap = 0
    team = []
    cardsInHand = []
    cardShop = []
    drawPile = []
    discardPile = []
    super().__init__()
  
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

class Enemy(Stats):
  def __init__(self):
    description = ""
    type = ""
    super.__init__()

  def setDescription(self, text):
    self.description = text

  def setType(self, TYPE):
    self.type = TYPE
  
  def getDescription(self):
    return self.description
  
  def getType(self):
    return self.type

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

class BoardState():
  def __init__(self):
    turn = 0
    currentLeyline = []
    leylinePile = []
    usedLeyline = []
    phase = 0  #0 is player, 1 is enemy

  def setBoardState(self, TURN, CLL, LLP, ULL, PHASE):
    self.turn = TURN
    self.currentLeyLine = CLL
    self.leylinePile = LLP
    self.usedLeyline = ULL
    self.phase = PHASE

  def getTurn(self):
    return self.turn
  
  def getCurrentLeyline(self):
    return self.currentLeyline
  
  def getLeylinePile(self):
    return self.leylinePile
  
  def getUsedLeyline(self):
    return self.usedLeyline
  
  def getPhase(self):
    return self.phase
  
  def incrementTurn(self):
    self.turn += 1
    if self.turn == 12:
      pass #flag for game over

  def drawLeyline(self):
    cardsToDraw = 0
    
    if self.turn < 2:
      cardsToDraw = 0
    elif self.turn <= 5:
      cardsToDraw = 1
    elif self.turn <= 8:
      cardsToDraw = 2
    else:
      cardsToDraw = 3

    if len(self.leylinePile) < cardsToDraw:
      random.shuffle(self.usedLeyline)
      self.leylinePile.append(self.usedLeyline)
      self.usedLeyline = []

    for i in range(cardsToDraw):
      currentLeyline = self.leylinePile[0]
      self.leylinePile.pop(0)
      self.currentLeyLine.append(currentLeyline)

  def switchPhase(self):
    if self.phase == 0:
      self.phase = 1
    else:
      self.phase == 0

if __name__ == '__main__':
  x = BoardState()
  x.setBoardState(0,[],[],[],0)
  print(x.getTurn())
  print(f"turn is: {x.getTurn()}")
  print(f"phase is: {x.getPhase()}")
  x.incrementTurn()
  print(f"turn is: {x.getTurn()}")
  print(f"phase is: {x.getPhase()}")

  # print(x.getName())
  # print(x.getHealth())
  # x.decreaseHealth(13)
  # print(x.getHealth())