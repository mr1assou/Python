class Student:
    def __init__(self,name,id,cours_enrolled,annual_fees):
        self.name=name
        self.id=id
        self.course_enrolled=cours_enrolled
        self.annual_fees=annual_fees
    def __str__(self):
        return f"name:{self.name} id:{self.id} cours enrolled:{self.course_enrolled} annual_fees:{self.annual_fees}"
    def __lt__(self,other):
        if self.annual_fees<other.annual_fees:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.annual_fees>other.annual_fees:
            return True
        else:
            return False
class ArtsStudent(Student):
    def __init__(self, name, id, cours_enrolled, annual_fees,project_grade):
        super().__init__(name, id, cours_enrolled, annual_fees)
        self.project_grade=project_grade
    def __str__(self):
            return f"name:{self.name} id:{self.id} cours enrolled:{self.course_enrolled} annual_fees:{self.annual_fees} project_grade:{self.project_grade}"
class CommerceStudent(Student):
    def __init__(self, name, id, cours_enrolled, annual_fees,internat_company):
        super().__init__(name, id, cours_enrolled, annual_fees)
        self.internat_company=internat_company
    def __str__(self):
        return f"name:{self.name} id:{self.id} cours enrolled:{self.course_enrolled} annual_fees:{self.annual_fees} internat_company:{self.internat_company} "
class TechStudent(Student):
    def __init__(self, name, id, cours_enrolled, annual_fees,project_grade,internat_company):
        super().__init__(name, id, cours_enrolled, annual_fees)
        self.project_grade=project_grade
        self.internat_company=internat_company
    def __str__(self):
        return f"name:{self.name} id:{self.id} cours enrolled:{self.course_enrolled} annual_fees:{self.annual_fees} internat_company:{self.internat_company}  project_grade:{self.project_grade}"
#object
