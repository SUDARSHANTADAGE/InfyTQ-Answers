'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
'''

#PF-Assgn-30

def encode(message):
    st=message+"0"
    l=[]
    count=1
    #Remove pass and write your logic here
    for i in range(0,len(st)-1):
        if st[i]==st[i+1]:
            count=count+1
        else:
            l.append(str(count))
            l.append(st[i])
            count=1
    s="".join(l)
    return s
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
