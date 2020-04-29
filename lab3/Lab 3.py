#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time, math
from graphics import *

####################
#### Question 1
####################

win = GraphWin("Question 1", 600, 600)
mouse1 = win.getMouse()
m1X,m1Y = mouse1.getX() , mouse1.getY()
m1_label = Text(Point(m1X,m1Y),"("+str(m1X)+","+str(m1Y)+")")
m1_label.draw(win)
mouse2 = win.getMouse()
m2X,m2Y = mouse2.getX() , mouse2.getY()
m2_label = Text(Point(m2X,m2Y),"("+str(m2X)+","+str(m2Y)+")")
m2_label.draw(win)
slope = (m2Y - m1Y) / (m2X - m1X)
line = Line(mouse1,mouse2)
line.draw(win)
#print(slope)
slope_t = Text(Point(300,10),"slope is "+str(round(slope,2)))
slope_t.draw(win)
time.sleep(4)
win.close()


# In[7]:


####################
#### Question 2
####################

#length is 2x of width
#to change the dimension, change the width varible from 400 to desired and everything else will run smoothly
width = 200
win1 = GraphWin("Question 2", 2*width, width)
win1.setCoords(0.0, 0.0, 3.0 , 3.0 )
b1 = Polygon (Point (0,0), Point(3,0),
Point (3,1), Point (0,1))
b2 = Polygon (Point (0,2), Point(3,2),
Point (3,3), Point (0,3))
b3 = Polygon (Point (0,1), Point(3,1),
Point (3,2), Point (0,2))
tri = Polygon (Point (0,0), Point(1.1,1.5),
Point (0,3))
b1.setFill (color_rgb ( 0, 119 ,139 ) )
b2.setFill (color_rgb ( 0, 119 ,139 ) )
b3.setFill (color_rgb ( 255 , 199 , 44 ))
tri.setFill ("black")
b1.draw(win1)
b2.draw(win1)
b3.draw(win1)
tri.draw(win1)
time.sleep(4)
win1.close()


# In[8]:


####################
#### Question 3
####################

win2 = GraphWin("Question 3", 500, 500 )
#grass
m1 = win2.getMouse()
m1_height = m1.getY()
grass = Polygon (Point (0,m1_height), Point(500,m1_height), Point (500,500) ,
Point (0,500))
grass.setFill ("green")
grass.draw(win2)
#sea
m2 = win2.getMouse()
m2_height = m2.getY()
sea = Polygon (Point (0,m2_height), Point(500,m2_height), Point (500,m1_height) ,
Point (0,m1_height))
sea.setFill ("blue")
sea.draw(win2)
# sky
"""could not set my student number as rgb value
my number is 101166611 whose last 3 digit 611 > 240 fails"""
sky = Polygon (Point (0,0), Point(500,0), Point (500,m2_height) ,
Point (0,m2_height))
sky.setFill (color_rgb ( 135, 206, 235 ))
sky.draw(win2)
# sun center
m3 = win2.getMouse()
m3x,m3y = m3.getX(),m3.getY()
m4 = win2.getMouse()
m4x,m4y = m4.getX(),m4.getY()
rad = math.sqrt((m4x-m3x)**2 + (m4y-m3y)**2)
sun = Circle(m3,rad)
sun.setFill ("orange")
sun.draw(win2)

time.sleep(3)
win2.close()


# In[ ]:




