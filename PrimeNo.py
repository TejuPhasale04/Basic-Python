num=int(input("Enter A Number::"))
flag=0
for i in range(2,num+1):
    if num%i:
        flag=1
        break
if(flag==0):
    print ("Number is prime")
else:
    print("Number is Not prime")