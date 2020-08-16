#It shows error in set_name method dont know why but satisfy all testcases

#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
        
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    def set_gender(self,gender):
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
                                        
Athlete("Maria","F")
Athlete.set_name("Maria")
Athlete.set_gender("F")
print(Athlete.get_name())
print(Athlete.running())
