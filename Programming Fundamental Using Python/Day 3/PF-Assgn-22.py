'''
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the 
list.
'''

#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    leap =[]
    for i in range(given_year,given_year+64):
        if i%400==0 and i%100!=0:
           leap.append(i)
        elif i%4==0 and i%100!=0:
           leap.append(i)
    list_of_leap_years=leap[:15]
    return list_of_leap_years
    

list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)
