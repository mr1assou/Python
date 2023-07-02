class student:
    error_name=["hamza","raghad","younes","malika","mohammadine"]
    x=0
    def __init__(self,name,gender,middlename) -> None:
        self.name=name
        self.gender=gender
        self.mid_name=middlename
        student.x+=1
    def get_display(self):
        if self.name in student.error_name:
            return  "the name is error"
        else:
            return f"the name is available"
    def delete_user(self): 
        student.x-=1
        return f"delete user {self.name}"    
    @classmethod
    def users_count(cls):
        print(f"users name in our system {cls.x}") 
    @staticmethod
    def say_hello():
        print("hello from static method")
print(student.x)
obj1=student("marwane",19,"assou")
obj2=student("marwane",19,"assou")
obj3=student("marwane",19,"assou")
obj4=student("hamza",19,"assou")
print(student.x)
print(obj4.delete_user())
print(f"{student.x}")
print(student.x)
print(student.users_count())
print("##############################")
print(obj1.users_count())
student.say_hello()
