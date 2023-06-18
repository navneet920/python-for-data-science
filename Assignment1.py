#WAP to input a string and count the number of uppercase and lowercase letters
'''
str=input("Enter string ")  
u,l=0,0
for i in str:
    if (i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1
print("Uppercase",u,"lowercase",l)        
'''

#WAP a python program to remove charecters that have odd index values in a given string
'''
str=input("Enter string :")
print(str[::2])
'''

#WAP a python program to get a string made first 2 and last 2 charecters of a given string if the string lenghtis less than 2,return the empty string instead
str=input("Enter string :")
if(len(str)<2):
    print("")
else:    
    print(str[0:2:1],end="")
    print(str[-2::])