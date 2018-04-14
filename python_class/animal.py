class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self    

    def displayHealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5  
        return self  

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
    
    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print("I am a Dragon")    


animal1 = Animal("Bobcat", 200)
dog1 = Dog("Fido", 300)
dragon1 = Dragon("Bob", 250)

print animal1.walk().walk().walk().run().run().displayHealth()
print dog1.walk().walk().walk().run().run().pet().displayHealth()
print dragon1.displayHealth()
