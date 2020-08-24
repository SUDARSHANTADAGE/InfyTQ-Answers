#OOPR-Assgn-19
#Start writing your code here
destination_list=["Mumbai","Pune","Chennai","Kolkata"]

class Ticket:
    counter=0
    
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None #Ticket.counter+1
        
    def validate_source_destination(self):
        if self.__source.title()=="Delhi":
            if self.__destination.title() in destination_list:
                return True
        return False
            
    def generate_ticket(self):
        Ticket.counter += 1
        if self.validate_source_destination():
            if Ticket.counter<10:
                self.__ticket_id=self.__source[0]+self.__destination[0]+"0"+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)
                
    def get_ticket_id(self):
        return self.__ticket_id
        
    def get_passenger_name(self):
        return self.__passenger_name
        
    def get_source(self):
        return self.__source
        
    def get_destination(self):
        return self.__destination
