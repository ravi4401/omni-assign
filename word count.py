my_data=open("data.txt","r") #### total words
data=my_data.read().split()
k=len(data)
print(k)


###word count
count=0
word=input()
for i in data:
    if word ==i:
        count+=1
print(count)
ratio=(count/k)  ###ratio for count/total words
print("word to the ratio of total" ,"%.2f"%ratio)

###character count
f1= open("data.txt","r")
data= f1.read()
count=0
print (type(data))
for i in data:
    if i == " ":
        continue
    else:
        count+=1
print (count)
