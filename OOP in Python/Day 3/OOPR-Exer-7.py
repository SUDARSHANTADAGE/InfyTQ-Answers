#OOPR-Exer-7
#Start writing your code here

class Ticket:
    counter=0
    
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None
        
    def validate_source_destination(self):
        dest=['Mumbai','Pune','Chennai','Kolkata']
        if self.__source.lower()=="delhi":
            if self.__destination.title() in dest:
                return True
            else:
                return False
        else:
            return False
            
            
    def generate_ticket(self):
        Ticket.counter +=1 
        if self.validate_source_destination():
            if Ticket.counter<10:
                self.__ticket_id=self.__source[0]+self.__destination[0]+'0'+str(Ticket.counter)
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
        
        
t=Ticket("Sudarshan","Delhi","Mumbai")
Ticket.counter=9
t.generate_ticket()
print(t.get_ticket_id())
print(t.get_passenger_name())
print(t.get_source())
print(t.get_destination())
t.generate_ticket()
print(t.get_ticket_id())
