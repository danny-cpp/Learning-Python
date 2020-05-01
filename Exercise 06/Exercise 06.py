#Exercise 06 - Vinh Nguyen - vinhhnguyen313@gmail.com
#April 25, 2020.
#This program involves calculating trajectories for different starting
#conditions of a projectile

import matplotlib.pyplot as plot
from numpy import arange


def dropit(A,vx0):
    x0 = 0
    t = 0.0
    dt = .1
    y = []
    x = []
              
    while(t<=30.0):
        if((len(y)!=0 and not y[-1]>=0) or ( (A - 1/2*(32.17)*t**2)<0)):
            break
        y.append( (A - 1/2*(32.17)*t**2) )
        x.append(vx0*t)
        if(t==30 and y > 0):
            print("The calculation is not finished, object is still falling")
        t += dt
    return [t,x[-1],y[-1]]

print("Exercise 06 - Vinh Nguyen - vinhhnguyen313@gmail.com\n\
April 25, 2020.")
print("This program simulates a falling object released from \
an airplane over and over again with many different starting conditions.")
print("-------------")

A, vx0 = map(float,input("Please enter the altitude (in feet) and the airspeed \
of the aircraft when the object is dropped, in knots (nautical miles per hour): ").split(","))


print("")
print("Your altitude is "+ str(A))
print("Your aircraft's airspeed is "+ str(vx0)+"\n")

print("TABLE OF RESULTS:")
print("%-15s %-18s %-15s %-15s" % ("Altitude (m)","Airspeed (knots)","Time (s)","Position (meters,meters)"))

altrange = arange(A+100,A-100, -200/9) if (A-100)>0 else arange(A+100,0,-(A+100)/9)

for i in altrange:
    for j in arange(vx0-10, vx0+10, 20/5):
        result = dropit(i,j*6076/60/60)
        print("%-15.2f %-18.2f %-15.2f (%3.2f, %3.2f)" % (i, j, result[0],result[1],result[2]))

