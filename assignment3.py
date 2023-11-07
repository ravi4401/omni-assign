a=input("enter card number:" )## input card number

my_list=list(a)
#print(type(my_list))

removed_last_digit=my_list[0:-1] #last digit removed
#print(removed_last_digit)

reverse_list=removed_last_digit[ : :-1]
#print(reverse_list)

#double the even indexes
panzer=[]


distance=len(reverse_list)
#finding indexed

for i in reverse_list:
    int_max=int(i)
    panzer.append(int_max)
    
for m in range(distance):
    if m%2==0:
        panzer[m]=panzer[m]*2

for n in range(distance):
    if panzer[n]>9:
        panzer[n]=panzer[n]-9

number_list=int(my_list[-1])


total_card_number=sum(panzer,number_list)

if total_card_number%10==0:
    print("card number is valid use card")
else:
    print("card number is invalid don't use card")