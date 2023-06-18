print("Welcome to Blood Donation Campus")
age=int(input("Enter age"))
if(age>=19):
    weight=int(input("Enter weight "))
    if(weight>=45):    
        height=int(input("Enter height"))
        if(height>=156):
            bg=input("Enter blood group")
            if(bg=='o+' or bg=='o-' or bg=='B+' or bg=='B-'):
                print("Your elligible for blood donation")
            else:
                print("Your blood group is not match :")
        else:
            print("Your are under height :")
    else:
        print("Your are under weight :")                    
else:
    print("Sorry you are not elligible")
    

