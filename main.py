from types import BuiltinMethodType






class fighter: 
  hp = 100
  name = "Vasto"
  age = "20"
  job = "fighter"
  attack = "60"
  can_use_items = True


class beserker:
  hp = 250
  name = "noam"
  age = "20"
  job = "beserker"
  attack = "100"
  can_use_items = True

# class person:
#   def __init__(self, hp, attack, defense, item usage, backpack storage):
#     self.hp = hp
#     self.attack = attack

# Fighter1 = person(100, 60)
# Archer1 = person(250, 100)
# Mage1 = person(100, 50)
# print(fighter.attack)

class student:
 def __init__(self, name, age, food):
   self.name = name
   self.age = age
   self.food = food


youssouf = student("youssouf", 20, "chicken")
print(youssouf.food)


# class person:
#   def __init__(self, hp, attack, defense, item usage, backpack storage):
#     self.hp = hp
#     self.attack = attack





