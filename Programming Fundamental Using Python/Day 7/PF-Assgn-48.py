'''
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.
'''

#PF-Assgn-48

def find_correct(word_dict):
    #start writing your code here
    correct,almost,wrong=0,0,0
    for key,value in word_dict.items():
        if key==value:
            correct=correct+1 
        else:
            if len(key)!=len(value):
                wrong=wrong+1
                continue
        incorrect=0
        for i in range(min([len(key),len(value)])):
            if key[i]!=value[i]:
                incorrect=incorrect+1 
                if incorrect>2:
                    wrong=wrong+1
                    break
        if 0<incorrect<3:
            almost=almost+1 
    return[correct,almost,wrong]
    
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
