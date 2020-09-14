#OOPR-Assgn-34
class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False
#Implement the class here
class PermanentEmployee(Employee):
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list,p_incentive):
        super().__init__(emp_id,e_incentive, job_level,salary, performance_list)
        self.__p_incentive=p_incentive
        
    
    def get_p_incentive(self):
        return self.__p_incentive
        
    def identify_performance_hike(self):
        performance_list=self.get_performance_list()
        if performance_list[4]==1 and performance_list[3]==1:
            hike=5 
        elif performance_list[4]==1 and performance_list[3]==2 and performance_list[2]==1:
            hike=3 
        else:
            hike = None
        return hike
        
    def identify_job_level_hike(self):
        job_level = Employee.get_job_level(self)
        if job_level in Company.dict_hike.keys():
            job_hike=Company.dict_hike[job_level]
            return job_hike
        else:
            return None
            
    def identify_incentive(self):
        c_incentive=Company.get_c_incentive()
        e_incentive=Employee.get_e_incentive(self)
        incentive=e_incentive + self.__p_incentive + c_incentive
        return incentive
        
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            Employee.update_salary(self, hike, incentive)
            return True
        else:
            return False
            
p = PermanentEmployee(2134,1000,"A",130000,[1, 2, 1, 1, 1],3000)
