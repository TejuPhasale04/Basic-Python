num=int(input("Enter A Numer::"))
sum=0
while num>0:
    no=int(num%10);
    sum=sum+no
    num=num/10
print("Sum Of Digit:",sum)