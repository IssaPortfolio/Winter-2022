class Critter(object):
   """A virtual pet"""
   total = 0
   def __init__(self, name, last, age, DOB, color):
      print ("A new critter has been born!")
      self.name = name
      self.last = last
      self.age = age
      self.DOB = DOB
      self.color = color
      Critter.total = Critter.total + 1
      
   def __str__(self):
        rep = "Critter object\n"
        rep += "Name: " + self.name + "\n"
        rep += "Last: " + self.last + "\n"
        rep += "Age: " + str(self.age) + " years old\n"
        rep += "DOB: " + self.DOB + "\n"        
        rep += "Color: " + self.color + "\n"
        return rep
    
   def talk(self):
      print ("Hi. I'm an instance of class Critter.")

def main():

    crit1 = Critter("Mary", "Jane", 19, "09/03/2001", "Blue")
    crit1.talk()
    print(crit1)
    
    crit2 = Critter("Frank", "Smith", 23, "06/23/2000", "Yellow")
    crit2.talk()
    print(crit2)
    
    print("Total Critters: " + str(Critter.total))
    
main()