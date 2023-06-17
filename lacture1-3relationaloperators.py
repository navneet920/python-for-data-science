#Relational Operators
# <,>,<=,>=,==,!=
'''a,b=8,10
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)'''

#Logical operators
# (and ),(or),(not) are logical operator
a,b,c=10,23,40
print(a>b and b<c)
print(a>b or b<c)
print(not(a>b or b<c))

#Assignment Operators
# +=,-=,/=,*= is assignment operator
a,b=10,20
a+=b
a-=b
a*=b
a/=b
print(a)

#Identity Operators
a=9
b=9
z=a
print(a is b)
print(z is not b)
b=int(input("Enter the value of b "))
print(a is b)