from item import item
class phone(item):
    pay_rate=0.5
    def __init__(self, name: str, price: float, quantity=0,broken_phone=0):
        super().__init__(name, price, quantity)
        assert price>=0,f"price {broken_phone} is not greater than or equal to 0"
        self.broken_phone=broken_phone