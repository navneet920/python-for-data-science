#strings
'''
s="hello"
print(s[2])
print(s[-2])
'''
''''
s="hello"
for i in s:
    print(i)
'''
'''
#string lenght
s="hello"
print(len(s))
'''
#join two string
'''
s1="hello"
s2="world"
print(s1+s2)
print(s1*3)
'''

#string slicing
#variable[start:stop:<step>]
s="navneet kumar"
s1="123456asdf"
print(s[1:5:2])
print(s[:5])  #stsrts with 0 index till 4th index
print(s[::-1])  #Reverse the string slicing 
print(s[-4])
print(s[::2])   #starts with 0 index till the end and skip with one index 
print(s[-3:-1])
print(s[-1:-5:-2])
print(s[-1::-2])
print(s[:8:])
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
print(s1.isdigit())
print(s.isalpha())
print(s1.isalnum())
print(s.isspace())
print("*".join(s))
print(" ".join(s))
print(s.split('n'))


#WAP to input a string and count the number of letters,digit and special charecter in a string
'''
str=input("Enter any string :")
ch,d,s=0,0,0
for i in str:
    if(i.isalpha()):
        ch=ch+1
    elif(i.isdigit()):
        d=d+1
    else:
        s=s+1
print("Charecter",ch)
print("digit",d)
print("Special",s)
'''