from abc import ABCMeta,abstractclassmethod
class programming(metaclass=ABCMeta):
    @abstractclassmethod
    def has_oop(self):
        pass
class python(programming):
    def has_oop(self):
        return "yes"
    def say_hello(): 
        print(f"hello world!")
class pascal(programming):
    def has_oop(self):
        return "No" 
one=python()
print(one.say_hello())