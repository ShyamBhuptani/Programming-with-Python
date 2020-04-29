import re
file_name = "war_and_peace.txt"

f = open(file_name,"r", encoding='utf-8-sig')
f1 = open("Output.txt","w", encoding='utf-8-sig')
sum = 0
for i in f:
    sum += 1
    if i.strip():
        ne = re.split(r'\s',i)
        for x in ne:
            x = x.strip('",--')
            x = x.strip("';()!,.")
            if(x != ""):
                word_final = x[1:len(x)] + x[0] + "ay"
                i = i.replace(x,word_final)
        f1.write(i)
f.close()
f1.close()