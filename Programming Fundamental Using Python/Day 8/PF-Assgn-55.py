'''
Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.

Go through the below program and complete it based on the comments mentioned in it.


Note: Perform case sensitive string comparisons wherever necessary.

'''

#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    
    for i in ticket_list:
        string_list=i.split(":")
       # for val in string_list:
        if(string_list[2]==destination):
            count+=1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    
    l=[]
    temp=[]
    m=[]
    for i in ticket_list:
        string_list=i.split(":")
        l.append(string_list[0])
    for i in l:
        if i not in temp:
            temp.append(i)
    for i in temp:
        s1=0
        s1=l.count(i)
        s2 = str(i)+":"+str(s1)
        m.append(s2)
    return m
def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    l=find_passengers_per_flight()
    temp=[]
    final=[]
    for i in l:
        s=i.split(":")
        temp.append(s[1])
    temp.sort()
    sort=temp[::-1]
    for i in range(0,len(sort)):
        for val in l:
            s2=val.split(":")
            if sort[i] in s2:
                final.insert(i,val)
    return final 
#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
#find_passengers_per_flight()
print(sort_passenger_list())
