# convert seconds to day, hour, minutes, and seconds
sec=int(input("enter the second:"))
hour=sec/60/60
min=sec/60
day=sec/60/60/24
print("the time hour of this sec is {} hour".format(hour))
print("the time min of this sec is {} min".format(min))
print("the time day of this sec is {} days".format(day))