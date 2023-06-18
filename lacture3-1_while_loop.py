#WAP to print !1 to 10 
'''
i=1
while(i<=10):
    print(i)
    i+=1
'''
#WAP to sum of digit of a number
''' 
n=int(input("Enter any number "))
s=0
k=n
while(n!=0):
    r=n%10
    n=n//10
    s+=r
print("sum of digit of a number",k,"=",s)        
'''

#WAP to input a number and find whether it is armstrong number or not
'''
num=int(input("Enter any number "))
s=0
k=num
while(num!=0):
    r=num%10
    s+=(r*r*r)
    num=num//10
if(s==k):
    print("Armstrong number")
else:
    print("Not Armstrong number ")        
'''

#WAP to check whether a given number is pelindrome or not 
num=int(input("Enter any number "))
k=num
s=0
while(num!=0):
    r=num%10
    s=s*10+r
    num=num//10
if(s==k):
    print("Pellindrome number ")
else:
    print("Not Pellindrome number ")    

