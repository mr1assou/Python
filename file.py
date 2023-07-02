from abc import ABC,abstractclassmethod
class employee(ABC):
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    @abstractclassmethod
    def get_total_salary():
        pass
    @abstractclassmethod
    def print():
        pass
class engineer(employee):
    def __init__(self, name, emp_id, salary,speciality,experience,overtime_hours,overtime_hours_rate):
        super().__init__(name, emp_id, salary)
        self.speciality=speciality
        self.experience=experience
        self.overtime_hours=overtime_hours
        self.overtime_hours_rate=overtime_hours_rate
    def set_overtime_hours(self,x):
        self.overtime_hours=x
    def set_overtime_hours_rate(self,y):
        self.overtime_hours_rate=y
    def print(self):
        return f"name of enginner is {self.name} and id is {self.emp_id} and salary is {self.salary} his speciality is {self.speciality} and experience {self.experience} and overtime_hours {self.overtime_hours} and and overtime_hours_rate{self.overtime_hours_rate}"
    def get_total_salary(self):
        return f"total salary is {self.salary+(self.overtime_hours*self.set_overtime_hours_rate)}"
class sales(employee):
    def __init__(self, name, emp_id, salary,goss_sales,comission_rate):
        super().__init__(name, emp_id, salary)
        self.goss_sales=goss_sales
        self.comission_rate=comission_rate
    def set_goss_sales(self,x):
        self.goss_sales=x    
    def set_commission_rate(self,y):
        self.comission_rate=y
    def print(self):
        return f"name of enginner sales is {self.name} and id is {self.emp_id} and salary is {self.salary} his goss_sales is {self.goss_sales} and commission rate {self.comission_rate}"
    def get_total_salary(self):
        self.salary=(self.salary + self.goss_sales)*self.comission_rate
        return f"total salary is {self.salary}"
obj1=engineer("marwane",84727,"9387$","informatique","5ans","2h","4h")
obj2=sales("abdo",74676,19873,100,123)
#print(obj2.get_total_salary())
print(obj2.print())
        