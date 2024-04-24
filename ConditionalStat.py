
a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
if(a>b):
    print(a," is greater than ",b)
elif(a<b):
    print(a," is lesser than ",b)

match a:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _:
        print()