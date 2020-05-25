'''
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns 
the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately
  1. If a word has only vowels then retain the word as is
` 2. If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words
'''

#PF-Assgn-50
vowels=["a","e","i","o","u","A","E","I","O","U"]
def sms_encoding(data):
    #start writing your code here
    word=data.split()
    l=[]
    for i in word:
        temp=[]
        v=[]
        for value in i:
            if value not in vowels:
                temp.append(value)
        if len(temp)==0:
            temp.append(i)
        l.append("".join(temp))
    return " ".join(l)


data="I will not repeat mistakes"
print(sms_encoding(data))
