//PF-Exer-9

noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=0

//Write your code here
//Populate the variable: totalCookies
 takeoff=noOfFlightsTakeOff*seatingCapacityTakeOff
 landed=(noOfFlightsLanded*seatingCapacityLanded)//2
 totalCookies=2*(takeoff+landed)

//Do not modify the below print statement for verification to work
console.log(totalCookies)
