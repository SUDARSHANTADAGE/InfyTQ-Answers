'''
Consider that the human tower is to be performed on a stage and the stage has a maximum weight limit.

Write a python program to find the maximum number of people at the base level such that the total weight of tower does not exceed the 
maximum weight limit of the stage.

Assume that:
1. Each person weighs 50 kg
2. There will always be odd number of men at the base level of the human tower.
'''

#PF-Exer-32

def human_pyramid(no_of_people):
    if no_of_people==1:
        return 50
    else:
        return  no_of_people*50+human_pyramid(no_of_people-2)
def find_maximum_people(max_weight):
    no_of_people=0
    sum=0
    l=[]
    weight=max_weight//50
    if weight%2==0:
        weight=weight-1
    for i in range(1,weight+1,2):
        res=human_pyramid(i)
        if res>max_weight:
            no_of_people=i-2
            break
        if res==max_weight:
            no_of_people=i
    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1250)
print(max_people)
