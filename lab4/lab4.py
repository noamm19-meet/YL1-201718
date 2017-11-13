class Animal(object):
    def __init__(self , sound , name , age , favortie_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favortie_color = favortie_color
    def eat(self , food):
        print("yummy!!"+ self.name + " is eating " + food)
    def description(self):
        print(self.name + "is" + self.age + "years old and loves the colore" +  self.favorite_color)
    def make_sound(self):
        print(self.sound+" "+self.sound+" "+self.sound)
cat = Animal("miaoo"," cat", 3, "black")
cat.eat("meat")
cat.make_sound()



class person(object):
    def __init__(self , name , age , gender):
        self.name = name
        self.age  = age
        self.gender = gender
        



      
