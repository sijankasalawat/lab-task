# Write a Python program to sum three given integers. However, if two or more values are

# equal sum will be zero.

num1=int(input("enter first num:"))
num2=int(input("enter second num:"))
num3=int(input("enter third num:"))
sum=num1+num2+num3
print(sum)
if num1==num2 and num2==num3 :
    print("the sum is 0")
else:
    print("the sum is not 0")


