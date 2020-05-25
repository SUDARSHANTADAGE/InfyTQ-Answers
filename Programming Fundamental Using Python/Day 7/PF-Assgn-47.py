'''
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted 
message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

1. Assume that the sentence would begin with a word and there will be only a single space between the words.
2. Perform case sensitive string operations wherever necessary.
'''

#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    sentence=sentence.split(" ")
    l=[]
    v=["a","e","i","o","u","A","E","I","O","U"]
    for index,value in enumerate(sentence):
       # print(value)
        if index%2==0:
            s=value[::-1]
            l.insert(index,s)
        else:
            c=[]
            for i in value:
                if i not in v:
                    c.append(i)
            for j in value:
                if j in v:
                    c.append(j)
            d="".join(c)
            l.insert(index,d)
    return l

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
