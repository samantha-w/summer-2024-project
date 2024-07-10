## User 
## Attributes: name and email
## methods: __init__, login, logout



## Attributes: name and email
## Methods: __init__, login, logout
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged_in = False
    def login(self):
        self.logged_in = True
        print(f"{self.email} has logged in.")
    def logout(self):
        self.logged_in = False
        print(f"{self.email} has logged out.")

## Subclass: Cashier
## Attributes: till_id
## Methods: make_order, process_payment
class Cashier(User):
    def __init__(self, name, email, till_id):
        super().__init__(name, email)
        self.till_id = till_id
    def make_order(self):
        print(f"{self.email} is making an order.")
    def process_payment(self):
        print(f"{self.email} is processing a payment.")
## Subclass: Customer
## Attributes: shopping_cart
## Methods: order and complain
class Customer(User):
    def __init__(self, name, email, shopping_cart):
        super().__init__(name, email)
        self.shopping_cart = shopping_cart
        
    def order(self):
        print(f"{self.email} is ordering.")
    def complain(self):
        print(f"{self.email} is complaining.")


## Test 1 : timmy, tim@internship.com
user_1 = User("Timmy", "tim@internship.com")

print(user_1.name)
print(user_1.__dict__)

## Test 2 : create a customer named jimmy jimmy@coolperson.com , cart has eggs and bacon

user_2 = Customer("jimmy", "jim@int.com", ["eggs", "bacon"])
print(user_2.__dict__)

## Test 3 : create a cashier named jasmine jasmine@internship.com, till id is 772

user_3 = Cashier("jasmine", "jasmine@int.com", 772)
print(user_3.__dict__)

## Test 4 : checking commit 
user_4 = Cashier("sam", "jasmine@int.com", 772)
print(user_3.__dict__)




