'''
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the 
frequency itself separated by a space.

Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
'''

#PF-Assgn-56

def max_frequency_word_counter(data):
    data=data.lower()
    word=""
    frequency=0
    raw=data.split()
    temp=[]
    l=[]
    cnt=[]
    length=[]
    for val in raw:
        if val not in temp:
            temp.append(val)
    for i in temp:
        c=raw.count(i)
        s1=str(i)+" "+str(c) 
        cnt.append(c)
        l.append(s1)
    frequency=max(cnt)
    if cnt.count(frequency)>1:
        for i in range (0,len(cnt)):
            if cnt[i]==frequency:
                length.append(len(l[i]))
        m=max(length)
        i1=length.index(m)
        word=l[i1]
        print(word)
    else:
        num=str(frequency)
        for i in l:
            s=i.split()
            for val in s:
                if num in val:
                    word=s[0]
        print(word,frequency)
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    


#Provide different values for data and test your program.
data="Work Like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
