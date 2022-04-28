
class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property   #THIS IS THE GETTER
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
 
 
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight


instance = Box(10)

print(instance.weight)
instance.weight = 15 #AGAIN THIS IS SETTER SEE IT CHANGED THE VALUE OF WEIGHT
print(instance.weight)
#del instance.weight #if you uncomment this, print statement below will cause AttributeError
print(instance.weight)