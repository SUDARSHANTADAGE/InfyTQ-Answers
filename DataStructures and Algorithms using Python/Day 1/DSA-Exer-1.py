#DSA-Exer-1

def update_mark_list(mark_list, new_element, pos):
    #Write your logic here
    mark_list.insert(pos,new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    '''Remove pass and write your logic here to return a list containing
    the marks at pos1 and pos2 respectively.'''
    m_list=[]
    m_list.append(mark_list[pos1])
    m_list.append(mark_list[pos2])
    return m_list

#Provide different values for the variables and test your program
mark_list=[89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))
