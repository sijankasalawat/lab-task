sub1=int(input("enter your mark in computing:"))
sub2=int(input("enter your mark in programing:"))
sub3=int(input("enter your mark in math:"))
sub4=int(input("enter your mark in software design:"))
mark=(sub1+sub2+sub3+sub4)/4
print(mark)
if 71<=mark:
    print("you got distinction")
elif 61<=mark:
    print("you got first division")
elif 41<=mark:
    print("you score second division")
else:
    print("you are fail")


