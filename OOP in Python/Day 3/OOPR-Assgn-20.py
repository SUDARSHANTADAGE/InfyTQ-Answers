#OOPR-Assgn-20
#Start writing your code here

class Applicant:
    __application_dict={"A":0,"B":0,"C":0}
    __applicant_id_count=1000
    
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None 
        self.__job_band=None 
        
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1 
        self.__applicant_id = Applicant.__applicant_id_count
        
        
    def apply_for_job(self,job_band):
        if Applicant.__application_dict[job_band]==5:
            return -1
        else:
            Applicant.__application_dict[job_band]+=1 
            self.generate_applicant_id()
            self.__job_band=job_band
            
    @staticmethod
    def get_application_dict():
        return Applicant.application_dict()
        
    def get_applicant_id(self):
        return self.__applicant_id
        
    def get_applicant_name(self):
        return self.__applicant_name
        
    def get_job_band(self):
        return self.__job_band
        
        
        
a=Applicant("Jack")
a.apply_for_job("C")
a.apply_for_job("C")
a.apply_for_job("C")
a.apply_for_job("C")
print(a.apply_for_job("C"))
print(a.get_applicant_id())
#job_band-Aapplicant_name-Jack(Method invoked 5 times)
