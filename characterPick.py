import random

def pickCharacter(characters):
  picked = 0
  pickedCharacters = []
  while picked < 4:
    choice = input(f"Choose a character {picked + 1} {characters}:")
    if choice not in characters:
      print("Invalid choice")
    else:
       pickedCharacters.append(choice)
       characters.remove(choice)
       picked += 1
  print(pickedCharacters)
     
    
def gacha():
    characters = ["Diluc", "Venti", "Noelle", "Barbara", "Rosaria", "Hutao"]
    roll1 = random.choice(characters)
    characters.remove(roll1)

    roll2 = random.choice(characters)
    characters.remove(roll2)

    roll3 = random.choice(characters)
    characters.remove(roll3)

    roll4 = random.choice(characters)
    characters.remove(roll4)

    roll5 = random.choice(characters)
    characters.remove(roll5)

    pull = [roll1, roll2, roll3, roll4, roll5]
    # print(pull)
    return pull

wish = gacha()
pickCharacter(wish)

