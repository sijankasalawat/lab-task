Distance=4
velocity=25
T1=((Distance/velocity)*60)
# since the buss spend two min and each ten steps,so 2*10
T2=20
bus=T1+T2
print("total time taken by bus is {}").format(bus)
j1=((1/7)*60)
j2=((1/15)*60)
j3=((1/7)*60)
jog=j1+j2+j3
print("the total jogging time is {}").format(jog)
if bus<jog:
    print("jogging is faster")
else:
    print("bus is faster")