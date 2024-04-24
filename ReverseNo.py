num=int(input("Enter A Number::"))
digit=1
while(num>0):
    no=num%10
    digit=digit*10+no
    num=num/10

print(num);