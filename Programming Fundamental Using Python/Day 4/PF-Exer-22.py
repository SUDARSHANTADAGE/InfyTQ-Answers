#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    num=101
    src=source[:3]
    dest=destination[:3]
    for i in range(0,no_of_passengers):
        ticket_number_list.append(airline+":"+src+":"+dest+":"+str(num))
        num=num+1
    #Use the below return statement wherever applicable
    if len(ticket_number_list)>4:
        ticket_number_list=ticket_number_list[-5:]
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
