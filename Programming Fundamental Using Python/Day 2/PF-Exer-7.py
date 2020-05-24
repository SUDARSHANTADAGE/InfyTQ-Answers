#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult=37550
    child=adult/3
    service_ad = (adult*7)/100
    service_ch = (child*7)/100
    ticket_cost_ad=adult + service_ad 
    ticket_cost_ch=child + service_ch
    final_cost_ad = ticket_cost_ad-((ticket_cost_ad*10)/100)
    final_cost_ch = ticket_cost_ch-((ticket_cost_ch*10)/100)
    cost_ad = no_of_adults*final_cost_ad
    cost_ch = no_of_children*final_cost_ch
    total_ticket_cost=cost_ch+cost_ad
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)
