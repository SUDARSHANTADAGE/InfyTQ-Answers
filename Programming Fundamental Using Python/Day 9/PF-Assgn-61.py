#PF-Assgn-61
import re 
def validate_name(name):
    #Start writing your code here
    if 0<len(name)<16:
        if str.isalpha(name):
            return True
    return False
    
def validate_phone_no(phno):
    #Start writing your code here
    if len(phno)==10:
        if str.isdigit(phno):
            for i in phno:
                if phno.count(i)!=10:
                    return True
    return False

def validate_email_id(email_id):
    #Start writing your code here
    if re.search('@gmail.com$|@yahoo.com$|@hotmail.com$',email_id)!=None:
        if email_id.count('@')==1 and email_id.count('.com')==1:
            return True
    return False
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    if not validate_name(name):
        print("Invalid Name")
    if not validate_phone_no(phone_no):
        print("Invalid phone number")
    if not validate_email_id(email_id):
        print("Invalid email id")
    if validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id):
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
