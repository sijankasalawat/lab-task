a=int(input("enter a num for a:"))
b=int(input("enter second num for b:"))
c=int(input("enter another num for c:"))
if a<b and a<c:
    print("a is smallest ")
elif b<a and b<c:
    print("b is smallest")
else:
    print("c is smallest")