def enemy_fight():
  zone = []
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

def prep_enemies(common_enemy, royal_enemy, zone):
  #shuffle common enemy deck
  #shuffle royal enemy deck
  #3-2 flag (start with two)
  #royal
  r_enemies = royal_enemies[:3]
  royal_enemies = royal_enemies[3:]
  zone.append(royal_enemies)

  c_enemies = common_enemies[:2]
  common_enemies = common_enemies[2:]
  zone.append(common_enemies)

  c_enemies = common_enemies[:3]
  common_enemies = common_enemies[3:]
  zone.append(common_enemies)

  c_enemies = common_enemies[:2]
  common_enemies = common_enemies[2:]
  zone.append(common_enemies)

  c_enemies = common_enemies[:1]
  common_enemies = common_enemies[1:]
  zone.append(common_enemies)


  