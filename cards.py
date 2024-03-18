from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def getCards(characters):
  uri = "mongodb+srv://Klee:GenshinTarot@genshintarot.no45cbt.mongodb.net/?retryWrites=true&w=majority&appName=GenshinTarot"
  client = MongoClient(uri, server_api=ServerApi('1'))
  try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
      print(e)

  
  cards = client["GenshinTarotCards"]
  """
  shop_dict = {CardName: {card_data, quantity}}
  """
  shop_dict = {}
  deck_dict = {}
  shop = []
  deck = []
  for character in characters:
    characterCards = cards["Characters"].find_one( {"Name": {"$eq" : character}})
    normalAttack = characterCards["UnupgradedCards"]["NormalSkill"]
    elementAttack = characterCards["UnupgradedCards"]["ElementSkill"]
    normalAttackU = characterCards["UpgradedCards"]["NormalSkill"]
    elementAttackU = characterCards["UpgradedCards"]["ElementSkill"]

    normalAttackName = characterCards["UnupgradedCards"]["NormalSkill"]["Name"]
    elementAttackName = characterCards["UnupgradedCards"]["ElementSkill"]["Name"]
    normalAttackUName = characterCards["UpgradedCards"]["NormalSkill"]["Name"]
    elementAttackUName = characterCards["UpgradedCards"]["ElementSkill"]["Name"] 

    # shop.append(elementAttackName)

    for i in range(3):
      deck.append(normalAttackName)
      deck_dict[normalAttackName] = [normalAttack, i+1]

    for i in range(2):
      deck.append(elementAttackName)
      deck_dict[elementAttackName] = [elementAttack, i+1]

      shop.append(normalAttackUName)
      shop_dict[normalAttackUName] = [normalAttackU, i+1]

      shop.append(elementAttackUName)
      shop_dict[elementAttackUName] = [elementAttackU, i+1]

    print(shop)
    # print(deck)

       

getCards(['Noelle', 'Hutao', 'Venti', 'Barbara'])
  # b = list(character["Characters"].find({"Name": {"$ne":"Template"}}))
  # # print(b)
  # ch = [x["Name"] for x in b]
  # print(ch)

  # random.shuffle(ch)
  # print(ch)