#Exercise 04 - Vinh Nguyen - vinhhnguyen313@gmail.com
#March 23, 2020.
#This program computes the gross weight and CG position for a larger aircraft
#which may have many stations, and where the number of stations might vary

def checkCoG(cog):
    if(not (cog>31.5)):
        print("Warning: your CoG value is too far aft")
    elif(not(cog<37.5)):
        print("Warning: your CoG value is too far forward")
    return;

def checkWeight(cog,weight):
    if(cog > 32.9):
        if(weight>=1600):
            print("Warning: your weight value is outside of the appropriate range, too much")
    else:
        if(weight >= (cog*228.571429-5920)):
            print("Warning: your weight value is outside of the appropriate range, too much")

    return;

print("Exercise 04 - Vinh Nguyen - vinhhnguyen313@gmail.com\nMarch 23, 2020")
print("")

print('''This program computes the gross weight and CG position for a larger aircraft
which may have many stations, and where the number of stations might vary''')
print("")

print('''You will now enter your arm and weight values, remmember that there is
a weight limit''')
print("")


weight = []
arm = []
moment = []
cog = 0

stationAmt = int(input("First, please enter the number of stations: "))

for i in range(stationAmt):
    x,y = map(float, input("Please enter weight and arm (in weight,arm format) for station "+str(i+1)+" : ").split(","))
    if(x<0):
        print("Negative weights are not allowed, your weight will now be 0.")
        x=0
    print("You have successfully entered your weight and arm as " + str(x) + "lbs and " + str(y) +"inches.")
    weight.append(x)
    arm.append(y)
    moment.append(x*y)
    cog = sum(moment)/sum(weight) if sum(weight) != 0 else cog
    print("The total weight of the system is: " + str(sum(weight)) +"lbs")
    print("The center of gravity is "+str(cog)+" inches from the reference point")
    checkCoG(cog)
    checkWeight(cog,sum(weight))
    print("")

print("Final Report::: ")
print("There are "+str(stationAmt)+" stations in total")
print("The total weight of the system is: " + str(sum(weight)) +"lbs")
print("The center of gravity is "+str(cog)+" inches from the reference point")
checkCoG(cog)
checkWeight(cog,sum(weight))


    
