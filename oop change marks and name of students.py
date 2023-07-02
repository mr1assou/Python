# Write a Python class named Student with two attributes student_name, mark. Modify the attribute values of
# the said class and print the original and modified 
# values of the said attributes. 
class student:
    def __init__(self,student_name,mark):
        self.student_name=student_name
        self.previous_name=student_name
        self.mark=mark
        self.previous_mark=mark
    def change_attribute_name(self,new_name):
        self.previous_name=self.student_name
        self.student_name=new_name
        print(f"the previous name is {self.previous_name} and the new name is {self.student_name}")
    def change_attribute_mark(self,new_mark):
        self.previous_mark=self.mark
        self.mark=new_mark
        print(f"the previous mark is {self.previous_mark} and the new mark is {self.mark}")
object1=student("Marwane","12")
object1.change_attribute_mark(17)
print(object1.mark)