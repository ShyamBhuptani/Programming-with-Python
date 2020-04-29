#!/usr/bin/env python
# coding: utf-8

# In[1]:


##################################
#### Question 1
##################################
#used list as this lab is about list and string otherwise dictionary  will be best DS for this problem
month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
stone = ["Garnet","Amethyst","Aquamarine","Diamond","Emerald","Pearl","Ruby","Peridot","Sapphire","Opal","Topaz","Turquoise"]

def birthstone(mon):
    if mon in month:
        index = month.index(mon)
        return stone[index]
    else : 
        return "unavailable due to incorrect month name"

def main():
    month_ip = input("Please enter your birth month full month name, i.e January : ")
    res = birthstone(month_ip.strip().lower())
    print("Your birthstone is",res)

main()


# In[1]:


##################################
#### Question 2
##################################

#problem a
# I have used ord and chr functions to find the ascii and then add the key value instead of hardcoding it usign list of A to Z
def cipher():
    key_val = eval(input("enter the key (a numerical val) : "))
    string_ip = input("Enter your message :")
    string_ip = string_ip.replace(" ", "")
    print("The encrypted version is :",end=" ")
    for i in string_ip:
        i = ord(i)+ key_val
        print(chr(i),end="")
cipher()

#problem b
# Explaination for decipher the message : 
# 1. we can use common word list from https://www.wordfrequency.info/free.asp
# 2. then for first word, we need to deduct key value in the range of max ascii word so to make the intermediate word
# 3. then for each iteration, comapare the intermediate word if it is present in the wordlist
# 4. if the word exists, then using that key value, decipher all other words which can probably make meaningful sentance( here the 
# accuracy cannot be determined as many words can be created, we should use ML to solve this problem )


# In[2]:


##################################
#### Question 3
##################################
#problem a
print("****** Problem A starts *************")
def reverse():
    string_ip = input("Enter your message :")
    for i in string_ip.split():
        i = i[::-1]
        print(i,end=" ")
    print("\n")
reverse()
print("****** Problem A ends *************")

#problem b
print("****** Problem B starts *************")
file_name = "diary.txt"

f = open(file_name,"r", encoding='utf-8-sig')
f1 = open("Output.txt","w", encoding='utf-8-sig')
for i in f:
    if i.strip():
        for i in i.split():
            i = i[::-1]
            f1.write(i)
            f1.write(" ")
    else:
        f1.write("\n")
f.close()
f1.close()
print("****** Problem B ends and output.txt is created *************")


# In[ ]:




