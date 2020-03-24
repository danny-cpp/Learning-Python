#Exercise 03 - Vinh Nguyen - vinhhnguyen313@gmail.com
#March 21, 2020.
#This program accepts numerical data from the keyboard and use it to compute
#gross weight and CoG position of a small aircraft.

def checkCoG(cog):
    if(not (cog>31.5 and cog<37.5)):
        print("Warning: your CoG value is outside of the appropriate range")
    return;

def checkWeight(cog,weight):
    if(cog > 32.9):
        if(weight>=1600):
            print("Warning: your weight value is outside of the appropriate range")
    else:
        if(weight >= (cog*228.571429-5920)):
            print("Warning: your weight value is outside of the appropriate range")

    return;

print("Exercise 03 - Vinh Nguyen - vinhhnguyen313@gmail.com\nMarch 21, 2020")
print("")

print("This program accepts numerical data from the keyboard \
and use it to compute gross weight and CoG position of a small aircraft.")
print("")

print("You will now enter your arm and weight values, remmember that there is\
a weight limit")

x1 = float(input("Please enter your first arm value: "))
m1 = float(input("Please enter your first weight value: "))

print("")

totalWeight = m1
totalMoment = m1*x1
centerOfGravity = totalMoment/totalWeight

print("The total weight of the system is: " + str(totalWeight) +"lbs")
print("The Center of Gravity is: "+ str(centerOfGravity) + " inches from the reference point")
checkWeight(centerOfGravity,totalWeight)
checkCoG(centerOfGravity)

print("")

x2 = float(input("Please enter your second arm value: "))
m2 = float(input("Please enter your second weight value: "))

print("")

totalWeight += m2
totalMoment += m2*x2
centerOfGravity = totalMoment/totalWeight

print("The total weight of the system is: " + str(totalWeight) +"lbs")
print("The Center of Gravity is: "+ str(centerOfGravity) + " inches from the reference point")
checkWeight(centerOfGravity,totalWeight)
checkCoG(centerOfGravity)

print("")

x3 = float(input("Please enter your third arm value: "))
m3 = float(input("Please enter your third weight value: "))

print("")

totalWeight += m3
totalMoment += m3*x3
centerOfGravity = totalMoment/totalWeight

print("The total weight of the system is: " + str(totalWeight) +"lbs")
print("The Center of Gravity is: "+ str(centerOfGravity) + " inches from the reference point")
checkWeight(centerOfGravity,totalWeight)
checkCoG(centerOfGravity)

print("")

x4 = float(input("Please enter your fourth arm value: "))
m4 = float(input("Please enter your fourth weight value: "))

totalWeight += m4
totalMoment += m4*x4
centerOfGravity = totalMoment/totalWeight

print("")

print("The total weight of the system is: " + str(totalWeight) +"lbs")
print("The Center of Gravity is: "+ str(centerOfGravity) + " inches from the reference point")
checkWeight(centerOfGravity,totalWeight)
checkCoG(centerOfGravity)



