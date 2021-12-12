#Given a n-digit number. Find the sum of its digits.

n = int(input("Enter a number: "))
total = 0
while n>0:
    digits=n%10
    total=total+digits
    number=n//10
print("The sum of digits os the number entered is",total)