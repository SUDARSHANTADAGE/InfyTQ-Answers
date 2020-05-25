'''
Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in
the input list. If there are no duplicate values, it should return an empty list.

'''

#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    temp=[]
    for i in list_of_numbers:
        if list_of_numbers.count(i)>1:
            if i not in temp:
                temp.append(i)
    return temp

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
