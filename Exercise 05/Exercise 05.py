#Exercise 05 - Vinh Nguyen - vinhhnguyen313@gmail.com
#March 24, 2020.
#This program simulates a falling object
#released from an airplane in level flight at constant speed using a graph

import matplotlib.pyplot as plot

print("Exercise 05 - Vinh Nguyen - vinhhnguyen313@gmail.com\n\
March 24, 2020.")
print("This program simulates a falling object released from \
an airplane in level flight at constant speed.")
print("-------------")

A = float(input("Please enter the altitude (in feet) at which \
the object is dropped: "))
print("Your altitude is "+ str(A)+"\n")

vx0 = float(input("Now please enter the airspeed of the aircraft \
when the object is dropped, in knots (nautical miles per hour): "))*6076
print("Your aircraft's airspeed is "+ str(vx0)+"\n")

x0 = 0

t = 0.0
dt = .1
y = []
x = []
          
while(t<=30.0):
    if(len(y)!=0 and not y[-1]>=0):
        break
    y.append( (A - 1/2*(32.17)*t**2) )
    x.append(vx0*t)
    print("t = "+"{:.2f}".format(t)+", (x,y)="+"("+"{:.2f}".format(x[-1])+","\
         + "{:.2f}".format(y[-1])+")")
    if(t==30 and y > 0):
        print("The calculation is not finished, object is still falling")
    t += dt

plot.figure(figsize=(8,5))
plot.suptitle("Projectile of a falling object released from an \
airplane in level flight at constant speed.")
plot.xlabel("Horizontal Distance x (feet)")
plot.ylabel("Vertical Distance y (feet)")
plot.plot(x,y)

plot.savefig("Exercise 05 Graph")
plot.show()

    


    
          








