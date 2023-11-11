old_data=list(map(int,input().split()))#provide data by spaces
print(old_data)
new_data=[]
m=range(len(old_data))
for i in m:
    min_a=min(old_data)
    print (min_a)
    new_data.append(min_a)
    old_data.remove(min_a)
print(new_data)
#asscending order
