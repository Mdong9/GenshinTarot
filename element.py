class element():
  element1 = None
  def __init__(self):
    pass
  
  def applyElement(self, elem):
    if self.element1 == None:
      self.element1 = elem
      return 0
    elif self.element1 != elem:
      match elem:
        case "Anemo":
          print("Applied Anemo Reaction")
        case "Pyro": 
          print("Applied Pyro Reaction")
        case "Geo": 
          print("Applied Geo Reaction")
        case "Hydro": 
          print("Applied Hydro Reaction")
        case "Electro": 
          print("Applied Electro Reaction")
        case "Cryo": 
          print("Applied Cryo Reaction")
      return elem
    else:
      pass

  def getElement(self):
    return self.element1

 
# Driver program
if __name__ == "__main__":
    elem = "Cryo"
    elem2 = "Pyro"
    status = element()
    print(status.applyElement(elem))
    print(f"I applied {status.getElement()} as my first element")
    print(status.applyElement(elem2))



