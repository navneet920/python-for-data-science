#WAP to print simple interest
'''p=int(input("Enter the value of p"))
r=int(input("Enter the value of r"))
t=int(input("Enter the value of t"))
si=(p*t*r)/100
print("Simple Interest")
print(si)'''

#WAP to input temp. in celsius and then convert it into fahrenheit
'''c=float(input("Enter the temp. "))
f=c*(9/5)+32
print("Tmp. in Fahrenheit ")
print(f)'''

#WAP to calculate compound interest 
'''p=int(input("Enter the value of p : ")) 
r=int(input("Enter the value of r : "))
t=int(input("Enter the value of t : "))
n=int(input("Enter the value of n : "))
ci=p*(1+r/n)**(n*t)-p
print("Compound Interest = ",ci) '''


#WAP to find EMI 
'''p*r*((1+r)**n)/[(1+r)**n-1]
p=principal loan amount
n=loan tenure in months
r=monthly interest rate'''
'''p=int(input("Principal loan amount : "))
n=int(input("Loan tenure in month: "))
r=int(input("Monthly interest rate : "))
emi=p*r*((1+r)**n)/((1+r)**n-1)
print("EMI=",emi)'''

'''from math import *
p=int(input("Principal loan amount : "))
n=int(input("Loan tenure in month: "))
r=int(input("Monthly interest rate : "))
emi=p*r*pow((1+r),n)/(pow((1+r),n)-1)
print("EMI=",emi)'''


# WAP to convert kelvin
'''c=int(input("Enter the temp."))
k=c+273
print("Temp. in kelvin= ",k)'''


# WAP to area of triangle
'''from math import *
a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle=",area)'''

#WAP that reads a number seconds are prints it in form mins and seconds
t=int(input("Enter the time in second "))
m=int(t/60)
s=t%60
print(m,"mins and",s,"seconds")


