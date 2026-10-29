class Animal: #This is the main class.
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        pass
    
    def make_sound(self):
        pass  

class Lion(Animal): #This is a subclass of Animal class.
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self): 
        return(f"{self.name} roars loudly!") #This returns the sound made by the lion.

    def eat(self):
        return(f"{self.name} eats fresh meat.") #This returns the food eaten by the lion.
  
class Elephant(Animal):
    def __init__(self, name: str):
            super().__init__(name)

    def make_sound(self):
        return(f"{self.name} trumpets!") 

    def eat(self):
        return(f"{self.name} eats grass and fruits.")
    
class Monkey(Animal):
    def __init__(self, name: str):
            super().__init__(name)

    def make_sound(self):
        return(f"{self.name} chatters!")  

    def eat(self):
        return(f"{self.name} eats bananas.")

#Creating the animals and calling the methods.
lion = Lion("Simba")
elephant =  Elephant("Dumbo")
monkey = Monkey ("George")

#Printing the information about the animals.
print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")    


