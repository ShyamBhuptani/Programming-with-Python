#!/usr/bin/env python
# coding: utf-8

# In[22]:


####################
## Question 1
####################

#part a
from math import pi

class Spheres:
    
    def __init__(self, radius):
        self.radius = radius
        
    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return round(4*(pi)*(self.radius**2),2)
    
    def volume(self):
        return round((4/3)*(pi)*(self.radius**3),2)

x = Spheres(2)
print("radius of circle is",x.getRadius())
print("surface area of circle is",x.surfaceArea())
print("volume of circle is",x.volume())

#part b
dict_pro2 = {
    'Earth' : 6370,
    "Jupiter" : 69910,
    "Mercury" : 2440
}

for key,val in dict_pro2.items():
    print("****************************************************")
    instance = Spheres(val)
    print("The radius of",key,"is",instance.getRadius(),"km")
    print("The surface area of",key,'is',instance.surfaceArea(),"km square")
    print("The volume of",key,'is',instance.volume(),"km cube")
    


# In[33]:


####################
## Question 2
####################

#part a
class Movie:
    
    def __init__(self, title, year, rating, awards, cast, director):
        self.title = title
        self.year = year
        self.rating = rating
        self.awards = awards
        self.cast = cast
        self.director = director
        
    
    def __str__(self):
        return self.title + ' ('+ str(self.year) +')'
    
    def cast_list(self):
        for x in self.cast:
            print(self.title,"is starring",x)

#part b
LaLaLand = Movie("La La Land", 2016, 8, "Academy Award for Best Actress", ['Ryan Gosling','Emma Stone'], "Damien Chazelle")
# string method overrided
print(LaLaLand)
#list of cast
print("\nThe cast list is as below :")
LaLaLand.cast_list()


# In[46]:


####################
## Question 3
####################
class FantasyCharacter:
    def __init__(self,name,experience,health):
        self.name = name
        self.experience = experience
        self.health = health
    
    def feed(self):
        self.health = self.health*1.1
    
    def fight(self):
        self.experience = self.experience*1.05
        self.health=self.health*0.8

#New Fantasy Character class gandalf inheriting main fantasy character class
class Gandalf(FantasyCharacter):
    def __init__(self,name,experience,health,actor):
        FantasyCharacter.__init__(self,name,experience,health)
        self.actor = actor
        self.weapon = ["Wizard staff"]
    
    def extraWeapon(self,name):
        self.weapon.append(name)
    
    def weapons(self):
        for x in self.weapon:
            print(self.name,"has the weapon '"+str(x)+"'")
            
    def __str__(self):
        return self.name

G = Gandalf("Gandalf",100,120,"Sir Ian McKellen")
###
print("Intial weapons")
G.weapons()
print("\nAfter adding extra weapons")
G.extraWeapon("Glamdring")
G.extraWeapon("Narya")
G.weapons()

#using main class method
G.feed()
#after upgrade
print("After feed health",G.health)


# In[ ]:




