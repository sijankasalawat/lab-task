# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
# print ‘COMMON YEAR’.
# Hint: • a year is a leap year if its number is exactly divisible by 4 and is not

# exactly divisible by 100

# • a year is always a leap year if its number is exactly divisible by 400

time=int(input("enter the year:"))
if (time%4==0 and time%100!=0):
    print("the year is leap year")
else:
    print("this is not leap year")