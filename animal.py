class Animal:
    # initialize, e.g feed in name and age. The program requires it
    def __init__(self, name, age):
        # When we feed in name and age we save them in instance variables
        self.name = name
        self.age = age
        
    # instance method have access to instance variables
    def speak(self):
        # return "My name is Zorka and I am 12 years old"
        return f"My name is {self.name} and I am {self.age} years old"

    def intro(self):
        return f"I am {self.name}"



