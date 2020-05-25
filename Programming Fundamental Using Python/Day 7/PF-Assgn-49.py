'''
In a fair coin we have an equal chance (50%) of either getting a ‘head’ or ‘tail’.  That is if we toss the coin a large number of times
we would observe head approximately 50% of the time. Write a program to implement a biased coin toss where the chance of getting a head
is 70% (and tail 30%). That is if we invoke the program 1000 times we should see the head randomly approximately 700 times.
'''

#PF-Tryout
#Start writing your code here
import random

def biased_flip(prob_true):
        return random.random()<prob_true
        

head,tail=0,0
for i in range(1000):
    value=biased_flip(0.7)
    if value:
        head=head+1
    else:
        tail=tail+1
print("Heads: "+str(head))
print("Tails: "+str(tail))
