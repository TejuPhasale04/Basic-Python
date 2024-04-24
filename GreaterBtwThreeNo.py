num1=int(input("Enter a First Number::"))
num2=int(input("Enter a second Number::"))
num3=int(input("Enter a third Number::"))

if(num1>num2 and num1>num3):
    print("Greater Number:",num1)
elif (num2>num1 and num2>num3):
    print("Greater Number:",num2)
else:
    print("Greater Number:",num3)