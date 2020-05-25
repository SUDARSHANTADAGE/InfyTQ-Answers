'''
The python function, find_average() given below, is written to accept a list of marks and return the average marks. On execution, the
program is resulting in an error.

1: Add code to handle the exception occurring in the code.

2: Make the necessary correction in the program to remove the error.

3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.

'''

#PF-Exer-30

def find_average(mark_list):
    try:
        total=0
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except:
        print("some error occur")
m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))
