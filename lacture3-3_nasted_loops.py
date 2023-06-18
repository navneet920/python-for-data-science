#Nested loops
'''
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
'''

#WAP to print prime numbers 15 to 30
'''
for i in range(15,31):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,"is a prime number ")
'''
#WAP to print multiplication table of all the number from 1 to 10
'''
for i in range(1,11):
    print("table of ",i)
    for j in range(1,11):
        print(i,'*',j,"=",i*j)
'''       
 #WAP to print following pattern
'''
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
'''        

#WAP to print the following pattern full pyramid 
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print('*',end=" ")
    print()
'''            
#WAP to print the following pattern 
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#WAP to print the following pattern full pyramid 
'''
n=int(input("Enter any number "))
for i in range(1,n+1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
'''
#WAP to print the following pattern
'''
for i in range(1,5):
    k=65
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
'''
for i in range(1,):
    print(i)            
