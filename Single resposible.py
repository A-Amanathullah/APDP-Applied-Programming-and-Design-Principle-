from abc import ABC,abstractmethod

class Order():
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total
 

class IPayment_method(ABC):
    @abstractmethod
    def pay(self,security_code):
        pass


class Dabit(IPayment_method):
    def pay(self, security_code):
        print("processing debit payment")
        print(f"verifying security code: {security_code}")
        self.status= "paid"

class Cradit(IPayment_method):
    def pay(self, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        self.status = "paid"


class Bitcoin(IPayment_method):
    def pay(self, security_code):
        print("processing bitcoin payment")
        print(f"verifying security code: {security_code}")
        self.status = "paid"




order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
order.pay("debit", "123495")
