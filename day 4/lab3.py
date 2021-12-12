# Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#
# if employee is female, then she will work only in urban areas.
#
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
#
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#
# And any other input of age should print "ERROR".

a=int(input("enter your age"))
print("are you male or female")
g=str(input("enter male for m amd female for f:"))
 if g=="m" :
    if a<=20 and a>=20:
        print("he work in any place")
    elif a<=40 and a>=60:
        print("he will work in urban")
    elif:
        print("error")
 elif g=="f" :
     print("you only work in urban")
 else:
     print(error)




