l =list(input())
size=int ( len(l))
for i in range (size):
    for j in range (size):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print (l)###bubble sort