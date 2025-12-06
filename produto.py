class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def stock_addition(self,quantity):
        if quantity>0:
            self.quantity+=quantity
            print(1)
        else:
            print(0)

    def sell(self,quantity):
        if quantity<= self.quantity:
            self.quantity-= quantity
            print(1)
        else:
            print(0)

    def show_info(self):
        print(f"{self.name} {self.price} {self.quantity}")

produto1 = Product("Vaso", 19.99, 100)
produto1.stock_addition(-20)
produto1.stock_addition(20)
produto1.sell(50)
produto1.sell(100)
produto1.show_info()

