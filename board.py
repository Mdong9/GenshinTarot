import random

"""
Board State Class:
  1. Clock Turn
  2. Leyline modifiers
  3. Player Phase -> Enemy Phase
"""

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
  print(f"turn is: {x.getTurn()}")
  
  print("incrementing turn")
  x.incrementTurn()
  print(f"turn is: {x.getTurn()}")
  
  print(f"phase is: {x.getPhase()}")
  print("switching phase")
  x.switchPhase()
  print(f"phase is: {x.getPhase()}")