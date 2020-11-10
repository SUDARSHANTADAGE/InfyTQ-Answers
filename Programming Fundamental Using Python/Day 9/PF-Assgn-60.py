#PF-Assgn-60
def remove_duplicates(value):
    #start writing your code here
    l=[]
    temp=[]
    for i in value:
        l.append(i)
    for i in l:
        if i not in temp:
            temp.append(i)
    return "".join(temp)

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
