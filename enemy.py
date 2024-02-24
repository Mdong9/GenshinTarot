from stats import Stats
from player import Player

"""
Enemy Class:
  Variables:
    1. Type (Normal, Elite, Boss)
    2. Mora
    3. Health
    4. Guard
    5. Attack


"""

def prep_enemies(common_enemies, royal_enemies, zone):
  r_enemies = royal_enemies[:3]
  royal_enemies = royal_enemies[3:]
  zone.append(r_enemies)

  c_enemies = common_enemies[:2]
  common_enemies = common_enemies[2:]
  zone.append(c_enemies)

  c_enemies = common_enemies[:3]
  common_enemies = common_enemies[3:]
  zone.append(c_enemies)

  c_enemies = common_enemies[:2]
  common_enemies = common_enemies[2:]
  zone.append(c_enemies)

  c_enemies = common_enemies[:1]
  common_enemies = common_enemies[1:]
  zone.append(c_enemies)

  return zone, common_enemies, royal_enemies

class Enemy(Stats):
  def __init__(self):
    super().__init__()
    description = ""
    type = ""
    defeated = False
    covered = True
    attack_type = ""
    

  def setDescription(self, text):
    self.description = text

  def setType(self, TYPE):
    self.type = TYPE

  def setAttackType(self, TYPE):
    self.attack_type = TYPE

  def getDescription(self):
    return self.description
  
  def getType(self):
    return self.type

  def getAttackType(self):
    return self.attack_type


  def fight(self, player:Player):
    if self.getAttackType() == "normal":
      if player.getGuard() >= self.getAttack():
        player.decreaseGuard(self.getAttack())
      else:
        remaining_attack = self.getAttack()-player.getGuard()
        player.decreaseGuard(self.getAttack())
        player.decreaseHealth(remaining_attack)
    else:
      player.decreaseHealth(self.getAttack())

  def enemy_fight(player_zone):
    zone = player_zone
    '''
    [
    {[][][]elite}
    {[][]normal}
    {[][][]}
    {[][]}
    {[]}
    ]
    '''

    for subzone in zone:
      for enemy in subzone:
        if not enemy.isCovered():
          #enemy.attack(player)
          pass

if __name__ == '__main__':
  zz = ["a","b","c"]
  z = ["d", "e", "f","g","h","i", "j","k"]
  zzz = []
  a = prep_enemies(z,zz,zzz)
  # print(a)

  enemy = Enemy()
  enemy.setAttack(5)
  # enemy.setAttackType("normal")
  enemy.setAttackType("oh my godd i love hamborgor")
  print(f"Enemy attack is: {enemy.getAttack()}")
  print(f"Enemy type is: {enemy.getAttackType()}")

  p = Player()
  p.setHealth(10)
  p.setGuard(2)
  # p.setGuard(0)
  print(f"Player health is: {p.getHealth()}, and player guard is: {p.getGuard()}")

  # print(type(p))
  enemy.fight(p)
  print(f"Player remaining health is: {p.getHealth()}")