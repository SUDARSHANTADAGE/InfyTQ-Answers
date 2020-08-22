#OOPR-Exer-8
class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,jugglingitem):
        #write the code to make the juggler juggle
        print(self.__name+" is juggling with "+self.JugglingItem)

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
