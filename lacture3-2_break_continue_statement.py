#break and continue Statement 
'''
for i in range(1,11):
    if(i==5):
        break
       #continue
    else:
        print(i)
'''
#WAP input number whether number is prime or not
num=int(input("Enter any number "))
s=0
for i in range(1,num+1):
    if(num%i==0):
        s=s+1
if(s==2):
    print("Prime")
elif(s==1):
    print("not prime")
else:
    print("not prime ")


num=int(input("Enter any number "))
for i in range(2,num):
    if(num%i==0):
        print("not ")
        break
if(num==i):
    print("prime")    
