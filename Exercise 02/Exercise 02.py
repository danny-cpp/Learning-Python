#Exercise 02 - Vinh Nguyen - vinhhnguyen313@gmail.com
#March 19, 2020.
#This program computes both the total weight and the location of the CoG of a
#small aircraft having four stations.

print("Exercise 02 - Vinh Nguyen - vinhhnguyen313@gmail.com\nMarch 19, 2020")
print("This program computes both the total weight and the location of the CoG of a small aircraft having four stations.")
print("")
      
aircraftWeight = 1107 #lbs
aircraftArm = 34.15 #inches

pilotAndPassWeight = 340  #lbs
pilotAndPassArm = 39.12 #inches

baggageWeight = 10 #lbs
baggageArm = 63.77 #inches

fuelWeight = 135 #lbs
fuelArm = 42.22 #inches

totalWeight = aircraftWeight+pilotAndPassWeight+baggageWeight+fuelWeight

centerOfGravity = (aircraftWeight*aircraftArm+pilotAndPassWeight*pilotAndPassArm+baggageWeight*baggageArm+fuelWeight*fuelArm)/totalWeight

print("The total weight of the system is: " + str(totalWeight) +"lbs")
print("The Center of Gravity is: "+ str(centerOfGravity) + " inches from reference point")
