#!/usr/bin/env python
# coding: utf-8

# In[3]:


#################################
### Question 1
#################################

animals = ["Cow","Dogs","Chickens","Horses","Goats"]
sounds = ["moo","woof","cluck","neigh","baa"]

for i in range(5):
    print("""Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
And on that farm he had a {0} , Ee-igh, Ee-igh, Oh!
With a {1} , {1} here and a {1} , {1} there.
Here a {1} , there a {1} , everywhere a {1} , {1} .
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n""".format(animals[i],sounds[i]))


# In[20]:


#################################
### Question 2
#################################

# part a
import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    letters += string.ascii_uppercase
    letters += string.digits
    letters += "!@#$%^&*"
    return ''.join(random.choice(letters) for i in range(stringLength))
print("Random password is ",randomString())

#part b
f = open("password.txt","w")
f.write("100 different passwords are as below\n")
f.write("**************************** \n")
for i in range(100):
    f.write(randomString())
    f.write("\n")
f.close()


# In[13]:


#################################
### Question 3
#################################
import time, math
from graphics import *

#part a
def distance(point1,point2):
    x1,y1 = point1.getX() , point1.getY()
    x2,y2 = point2.getX() , point2.getY()
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)

#part b
def perimeter(polygon):
    perimeter = 0
    list_of_points = polygon.getPoints()
    for i in range(len(list_of_points)):
        z= 0 if i == len(list_of_points) -1 else (i+1)
        perimeter += distance(list_of_points[i],list_of_points[z])
    return round(perimeter,2)

#part c
Polygon = Polygon(Point(0,0), Point(2,0), Point(2,2),Point(0,2))
print("perimeter of above given polygon is" ,perimeter(Polygon))


# In[22]:


#################################
### Question 4
#################################
import matplotlib.pyplot as plt
#part a 
def convertor(listOfTFE):
    listOfCel = []
    for i in listOfTFE:
        cel = (i - 32) * (5/9)
        listOfCel.append(round(cel,2))
    return listOfCel

#part b
f = open("averageHighsOttawa.txt","r")
months = []
temps = []
for i in f:
    months.append(i[:3])
    temps.append(int(i[4:-1]))
print(temps)
celTemp = convertor(temps)
print(celTemp)

#part c
plt.bar(months,celTemp)
plt.xlabel("Month")
plt.ylabel("Temp in C")
plt.show()


# In[ ]:




