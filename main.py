# From File import Class
from animal import Animal 

dog = Animal(name = 'Lizzy', age = 3)
cat = Animal(name = 'Zorka', age = 10)
bird = Animal(name = 'Fufu', age = 5)

print(dog.speak())
print(cat.speak())
print(bird.speak())

print(dog.intro())
print(cat.intro())
print(bird.intro())



### print(dir(Animal)) to check methods which can be used.
### Returns a fault
# print (Animal.speak())

# instance / object
# dog = Animal()
# cat = Animal()

# print(dog.speak())
# print(cat.speak())

### This is used to find out the function / method used
### print(Animal.__dict__)

# -------------------------

# To progress further from above
# instance / object
# dog = Animal(name = 'Lizzy', age = 3)
# cat = Animal(name = 'Zorka', age = 10)
# bird = Animal(name = 'Fufu', age = 5)

# print(dog.speak())
# print(cat.speak())
# print(bird.speak())

# print(dog.intro())
# print(cat.intro())
# print(bird.intro())
