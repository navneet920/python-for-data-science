#syntax:
'''if(codition):
        #statements
    else:
            #statements    '''

#WAP to input a number and check whether it is positive or negative
'''num=int(input("Enter any number "))
if(num>0):
    print("positive")
else:
    print("Negative")   '''    

#WAP to check whether number is odd or even 
'''num=int(input("Enter any  number "))
if(num%2==0):
    print("Even number ")
else:
    print("Odd number ")'''        

#WAP to input a number and check whether it is divisible by 5 as well as 3 
'''n=int(input("Enter any number "))
if(n%5==0 and n%3==0):
    print("Number is divisible by 5 as well as 3")
else:
    print("Not divisible ") '''

#WAP to input a charecter and check whether vowel or consonant
'''ch=input("Enter any alphabet ")
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Alphabet is vowel")
else:
    print("Alphabet is consonant")'''           \
    

#Multiple conditional statement 
'''if(condition):
    statements
elif(condition):
    statements
elif(cindition):
    statements
else:
    statements'''

#WAP to input marks of a student and print their grade
#according to the following
#marks        grade
#90 to 100      A+
#80 to 90       A
#70 to 80       B+
#60 to 70       B
#50 to 60       C+
#40 to 50       C
#30 to 40       D
#less than 30   fail
'''marks=int(input("Enter tne marks"))
if(marks>=90 and marks<=100):
    print("Grade A+")
elif(marks>=80 and marks<90):
    print("Grade A")
elif(marks>=70 and marks<80):
    print("Grade B+")
elif(marks>=60 and marks<70):
    print("Grade B")
elif(marks>=50 and marks<60):
    print("Grade C+")  
elif(marks>=40 and marks<50):    
     print("Grade C")
elif(marks>=30 and marks<400):     
    print("Grade D")
else:
    print("Fail")   '''

#WAP to input three numbers and print the largest one 
'''num1=int(input("Enter 1st number "))
num2=int(input("Enter 1st number "))
num3=int(input("Enter 1st number "))
if(num1>num2 and num1>num3):
    print(Num1," is largest one ")
elif(num2>num3):
    print(Num2 ,"is largest one  ")
else:
    print(Num3," is largest one ")'''

#WAP to input a year and check whether it is leap or not
'''year=int(input("Enter any year "))
if((year%4==0 or year%100!=0) and (year%400==0)):
    print("Leap year")
else:    
    print("Not leap year")'''

#WAP to input number and make a calculater 
'''n1=int(input("Enter 1st number "))
n2=int(input("Enter 2nd number "))
op=input("Enter any operater ")
if(op=='+'):
    print(n1+n2)
elif(op=='-'):
    print(n1-n2)
elif(op=='*'):
    print(n1*n2)
elif(op=='/'):
    print(n1/n2)
elif(op=='%'):
    print(n1%n2)'''

#WAP to print the health status of a person by following 
#BMI                  wieght Status
#below 18.5           Underweight 
#18.5 to 24.9         Normal 
#25 to 29.0           overweight
#30.0 and above       obese
weight=int(input("Enter waight in kg "))
height=float(input("Enter height in metre "))
bmi=weight/(height**2)
print(bmi)
if(bmi>=30.0):
    print("Opese")
elif(bmi>=25 and bmi<=29.9):
    print("Overweight ")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal ")
else:
    print("Underweight ")            
          

