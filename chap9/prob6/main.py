class Critter(object):
 """A virtual pet"""
 def __init__(self, name):
  print("A new critter has been born!")
  self.__name = name
 @property
 def name(self):
  return self.__name
 
 @name.setter
 def name(self, new_name):
  if new_name == "":
    print("Name change successful.\n")
  else:
   self.__name = new_name
   print("A critter's name can't be the empty string.")
 def talk(self):
  print("\nHi, I'm", self.name)
# main
crit = Critter("Poochie")
crit.talk()
print("\nMy critter's name is:", end= " ")
print(crit.name)
print("\nAttempting to change my critter's name.")
crit.name = "Randolph"

print("\nAttempting to change my critter's name again")
crit.name = ""
print("Hi, I'm", end= " ")
print(crit.name)
input("\n\nPress the enter key to exit.")

