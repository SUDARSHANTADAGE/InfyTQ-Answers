#OOPR-Assgn-22
class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=["M-10",None]
    __list_ticket_price=[150,200]
    
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    
    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name.lower() not in Multiplex.__list_movie_name:
            return 0
        elif Multiplex.__list_total_tickets[Multiplex.__list_movie_name.index(movie_name)]<number_of_tickets:
            return -1
        else:
            movie_indx=Multiplex.__list_movie_name.index(movie_name)
            self.__seat_numbers=self.generate_seat_number(movie_indx, number_of_tickets)
            self.calculate_ticket_price(movie_indx, number_of_tickets)
            
        
        '''Write the logic to book the given number of tickets for the specified movie.'''
    
    def generate_seat_number(self,movie_index, number_of_tickets):
        
        prefix,tkt_list,number_of_tickets='',[],int(number_of_tickets)
        
        
        if movie_index == 0:
            if Multiplex.__list_last_seat_number[0] is None:
                lst_tkt=0
        
            else:
                lst_tkt=int(Multiplex.__list_last_seat_number[0].split('-')[-1])
            prefix="M1"
            
            for i in range (lst_tkt+1,lst_tkt+number_of_tickets+1):
                tkt_list.append(prefix+'-'+str(i))
            Multiplex.__list_last_seat_number[0]=tkt_list[-1]
            Multiplex.__list_total_tickets[0]-=number_of_tickets
        
        
        else:
            if Multiplex.__list_last_seat_number[1] is None:
                lst_tkt=0
            
            else:
                lst_tkt=int(Multiplex.__list_last_seat_number[1].split('-')[-1])
            prefix="M2"
            
            for i in range (lst_tkt+1,lst_tkt+number_of_tickets+1):
                tkt_list.append(prefix+'-'+str(i))
            Multiplex.__list_last_seat_number[1]=tkt_list[-1]
            Multiplex.__list_total_tickets[1]-=number_of_tickets

        return tkt_list


    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
   
    
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
