#OOPR-Assgn-13
#Start writing your code here

class Classroom:
    classroom_list=[]
        
    @staticmethod
    def search_classroom(class_room):
        for room in Classroom.classroom_list:
            if class_room.lower()==room.lower():
                return "Found"
        return -1
