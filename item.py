import csv
class item:
    pay_rate=0.8 #the pay after 20% discount
    all=[]
    def __init__(self,name: str,price:float,quantity=0):
        #Run validations to the recieved argements 
        assert price>=0,f"price {price} is not greater than or equal to 0"
        assert quantity >=0,f"price {quantity} is not greater than or equal to 0"
        #assign to self object
        self.__name=name 
        self.__price=price
        self.quantity=quantity
        #actions to excute
        item.all.append(self)
    @property
    def name(self):
        return self.__name 
    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("the name is too long")
        else:
            self.__name=value
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        self.__price=value
    def apply_discount(self):
        self.__price=self.price-self.__price*self.pay_rate 
    def calculate_total_price(self):
        return self.__price*self.quantity
    def apply_increment(self,increment_value):
        self.__price=self.__price+self.__price*increment_value
    def __connect(self,smpt_server):
        pass
    def __prepare_body(self):
        return f"""
        Hello someone.
        we have {self.__name} {self.quantity}.
        regards Marwane
        """
    def __send(self):
        pass 
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()    
    @staticmethod
    def is_integer(num):        
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__},'{self.name}','{self.price}','{self.quantity}'"