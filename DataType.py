#1. Numeric Types
#int
a = 5
b = -3456
c = 0
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print("Type of c: ", type(c))
print('*' * 30)

#floating point number
a = 5.0
b = -456.54
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print('*' * 30)

#Complex
a = 2 + 4j
b = 3 - 5j 
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print('*' * 30)


#2. Sequence Types
#a. Strings : 
str1='Hello Everyone\''
print("String with single quotes",str1)
str2="I am Tejaswini"
print("String with quable quotes",str2)
str3='''I am
            Futur 
                data scientist'''
print("String with triple quotes",str3)
print('*' * 30)

#List

lst1=[]
print("Empty List",type(lst1))
lst2=[1,34,4.5,"Tejaswini"]
print(("Type of lst2",type(lst2)))
print('*' * 30)

#Tuple
tpl=()
print("Type of tuple tpl=",type(tpl))
tpl2=(150,"Tejaswini",150,150)
print('*' * 30)

#Boolean
selected=True
print(type(selected))
print('*' * 30)

#set
set1={150,"Tejaswini","SCOE",150,150}
print(set1)
print("Type of set1=",type(set1))
print('*' * 30)

#Dictionary

Dict={"name":"Tejaswini"}
print("Dictionary:",type(Dict))
print('*' * 30)

Intro="My name is Tejaswini Phasale.I am from Nagar."
CurrentEdu="Currently I doing BTech in Information Technology"
print(Intro,end="$$")
print(CurrentEdu,end="\n")
print(Intro,CurrentEdu,sep="*******")
