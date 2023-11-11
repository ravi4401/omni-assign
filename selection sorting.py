#selection sorting in descending order 
old_data=list(map(int,input().split()))#provide data by spaces
print(old_data)
new_data=[]
m=range(len(old_data))
for i in m:
    max_a=max(old_data)
    print (max_a)
    new_data.append(max_a)
    old_data.remove(max_a)
print(new_data)





