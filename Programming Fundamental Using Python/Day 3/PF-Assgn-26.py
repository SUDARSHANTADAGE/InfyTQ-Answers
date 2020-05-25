'''
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
'''


#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if heads==(legs//2):
        chicken_count=heads
    elif heads==(legs//4):
        rabbit_count=heads
    elif legs%2==0:
        rabbit_count=(legs//2)-heads
        chicken_count=heads-rabbit_count
    else:
        print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    if chicken_count>0 or rabbit_count>0:
        if chicken_count<=heads and rabbit_count<=heads:
           print(chicken_count,rabbit_count)
        else:
           print(error_msg)

#Provide different values for heads and legs and test your program
#solve(38,131)
solve(20,10)
