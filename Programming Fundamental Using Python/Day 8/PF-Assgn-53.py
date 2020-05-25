'''
Assume that a poem is given. Write the regular expressions for the following:
1. Print how many times the letter 'v' appears in the poem.
2. Remove all the newlines from the poem and print the poem in a single line.
3. If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.
4. If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*.
'''

#PF-Assgn-53
#This verification is based on string match.

poem='''
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.
import re
#Write your logic here for question 1
count=0
for i in poem:
    if i == "v":
        count=count+1 
print(count)
print()
print(re.sub(r"\n",r" ",poem))

#print()
print(re.sub(r"ch",r"Ch",re.sub(r"co",r"Co",poem)))

#print()
print(re.sub(r"ai...",r"ai*/*",re.sub(r"hi...",r"hi*/*",poem)))
