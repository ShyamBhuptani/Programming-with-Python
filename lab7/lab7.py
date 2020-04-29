#!/usr/bin/env python
# coding: utf-8

# In[3]:


########################################
###### Question 1
#######################################

x = True
cost = 0.0
while(x):
    inp = input("Would you like to scan a page (yes/no)?")
    if(inp == "yes" or inp == "Yes"):
        x = True
        cost = cost + 0.05
        print("Subtotal: $"+str(round(cost,2)))
    elif (inp == "no" or inp == "No"):
        x = False
        print("Total : $"+str(round(cost,2)))
    else:
        print("Wrong Input")
        print("Total : $"+str(round(cost,2)))
        x = False
        


# In[22]:


########################################
###### Question 2
#######################################
from random import randint

def roll():
    return randint(1, 6) + randint(1, 6)

def craps():
    first = roll()
    if first in {2,3,12}:
        return 0
    elif first in {7,11}:
        return 1
    while True:
        roll_ = roll()
        if roll_ == first:
            return 1
        elif roll_ == 7:
            return 0
        
passed_cases = 0
for x in range(500):
    passed_cases += craps()
print("the estimated probability of winning is",passed_cases/500)


# In[ ]:


########################################
###### Question 3
#######################################

#part a
def check(string):
    if(len(string) != 3):
        print("Invalid string, length should be 3")
        return False
    i = 2
    list_codon = ["A","G","T","C"]
    res = False
    while i:
        if string[i] in list_codon:
            res = True
        else:
            res = False
            break
        i -= 1
    return res
#check("ABB")

#part b
x = True
while(True):
    inp = input("Please enter a codon : ")
    res = "Valid" if check(inp) == True else "Invalid"
    print("Your entred codon is",res)
    if(res == "Valid"):
        x = False
        break


# In[5]:


########################################
###### Question 4
#######################################

#part a
'''
Post test while loop will be helpful to stop determine stop codons and break the code
code will be like

while(string):
    if(string[slice] = END_CODONS):
    break
    
'''
#part b

string = "AAAATGACCACDACFTAGAAAATGACCACDACFTAG"
stop_codons = ["TAG","TAA","TGA"]
counter = 0
sums = 0
i = 0
codon = string[0:i+3]
while(i < len(string)):
    if(codon not in stop_codons):
        if(codon == "ATG"):
            counter += 1
        elif(counter > 0):
            counter += 1
        i += 3
        codon = string[i:i+3]
    else:
        sums +=  counter
        counter = 0
        i+=3
        codon = string[i:i+3]

print(sums)


# In[ ]:




