'''
There are two basketball teams (Team1 and Team2) in a school and they play some matches everyday depending on their time and interest. 
Some days they play 3 matches, some days 2, some days 1 etc.

Write a python function, find_winner_of_the_day(), which accepts the name of the winner of each match and returns the name of the overall 
winner of the day. In case of equal number of wins, return “Tie”.

'''

#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    t1=0
    t2=0
    for i in match_tuple:
        if i=="Team1":
            t1=t1+1
        else:
            t2=t2+1
    if t1>t2:
        #print("Team1")
        return "Team1"
    elif t2>t1:
        return "Team2"
    else:
        return "Tie"
#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
