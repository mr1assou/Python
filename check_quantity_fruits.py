"""
Define a Class Called Cart that Contains Data Attributes Apples and Oranges. Write Methods that
Return Appropriate Messages If the Number of Apples is Greater than 5 or When the Number of
Oranges are Greater than 10.
# Example usage
def main():
fruits = Cart(3, 11)
returned_apple_message = fruits.apple_quantity_check()
returned_orange_message = fruits.orange_quantity_check()
print(f"Apple is in {returned_apple_message}")
print(f"Orange is in {returned_orange_message}")
if __name__ == "__main__":
main()
Output
Apple is in Insuffiient Quantity
Orange is in Suffiient Quantity
"""
class cart:
    def __init__(self,apples,oranges):
        self.apples=apples
        self.oranges=oranges
    def apple_quantity_check(self):        
        if self.apples>5:
            return f"apples is in Suffiient Quantity"
        else:
            return "Apple is in Insuffiient Quantity"
    def orange_quantity_check(self):        
        if self.oranges>5:
            return f"oranges is in Suffiient Quantity"
        else:
            return "oranges is in Insuffiient Quantity"
    #call_object
def main():
    fruits = cart(3, 11)
    returned_apple_message = fruits.apple_quantity_check()
    returned_orange_message = fruits.orange_quantity_check()
    print(f"Apple is in {returned_apple_message}")
    print(f"Orange is in {returned_orange_message}")
if __name__ == "__main__":
    main()