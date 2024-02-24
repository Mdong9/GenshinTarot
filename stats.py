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

