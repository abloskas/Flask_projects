class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def displayInfo(self):
        print("Price: ${}, Name: {}, Weight: {} lbs, Brand: {}, Status: {}".format(self.price, self.item_name, self.weight, self.brand, self.status))
        return self

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        return self.price + self.price * tax    

    def returns(self, return_reason):
        if 'defective'in return_reason:
            self.status = 'defective'
            self.price = 0
        elif 'in box' in return_reason:
            self.status = 'for sale'
        elif 'opened'in return_reason:
            self.status = 'used'
            self.price = self.price * .80
        return self

product1 = Product(500, "laptop", .25, "Toshiba")   

print product1.returns('opened')     
print product1.price

