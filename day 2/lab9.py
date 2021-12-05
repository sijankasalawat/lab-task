 # Given the integer N - the number of minutes that is passed since midnight - how many

#hours and minutes are displayed on the 24h digital clock?
t=int(input("enter the time:"))
hour=t//60
minutes=t%60
print(hour,minutes)