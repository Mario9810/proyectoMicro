f = open("data.txt","r")

text = f.read()
count = 0
count2 = 0
for i in text:
    count2 += 1
    if i == "1":
        count+=1
        
print(count)
print(count2)