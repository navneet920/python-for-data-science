#1.for loop  --> A counting loop..............
#2. while loop   -->Conditional loop..........
#range() function
#range(strat,stop,step)
#range(1,10) --> 1,2....,9
#range(5,10)  -->  5,6,...,9
#range(1,10,2)  -->1,3,5,7,9
#range(10,0,-1)  --> 10,9,8,......,1
#for variable in <sequence>

#for i in range(1,21):
#    print(i)
 
#WAP to print all even numbers and odd numbers from 10 to 20 
'''
for i in range(10,20):
    if(i%2==0):
        print(i)
for i in range(10,20):
    if(i%2!=0):   
        print(i)  
'''
#WAP sun of even and odd number between 10 to 20
'''
se=so=0
for i in range(10,21):
    if(i%2==0):
        se+=i
    else:
        so+=i
print(se,so)
'''        
#WAP to input print its factorial using for loop
'''
n=int(input("Enter any number "))
f=1
for i in range(1,n+1):
    f*=i
print("Factorial of",n,"=",f)      
'''

#WAP to print following fibonacci series using for loop:
'''
n1,n2=0,1
print(n1,n2,end=' ')
for i in range(1,30):
    a=n1+n2
    print(a,end=' ')
    n1=n2
    n2=a
'''

#WAP to print the following series:   1/1!+1/2!=1/3!+.......
'''
n=int(input("ENter any number "))
for i in range(1,n+1):
    if(i<n):
        print("1/",i,'! + ',end='')
    else:
        print("1/",i,'!')
'''
#WAP to print sum of above series
'''
n=int(input("ENter any number "))
f=1
s=0
for i in range(1,n+1):
    f*=i
    s=s+1/f
print(s)     
'''