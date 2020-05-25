'''
Write a python function, check_anagram() which accepts two strings and returns True, if one string is an anagram of another string. 
Otherwise returns False.

The two strings are considered to be an anagram if they contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
'''

#PF-Assgn-54
def check_anagram(data1,data2):
    #start writing your code here
    l1=[]
    l2=[]
    for i in data1.lower():
        l1.append(i)
    for i in data2.lower():
        l2.append(i)
    c=0
    if len(data1)==len(data2):
        for i in range(0,len(data1)):
            if l1[i] in l2 and l1[i]!=l2[i]:
                c=c+1 
    else:
        return False
    if len(data1)==c:
        return True
    else:
        return False

print(check_anagram("About","table"))
