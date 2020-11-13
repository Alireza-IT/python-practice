# class Product:
#     def __init__(self, price):
#         # self.__price = price
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             return ValueError("price can not be negative")
#         self.__price = value


# product = Product(-50)  # can get negative vale which is not good
# first solution is that make the attribute private and make set and get for that

# this solution is ugly

# PROPERTY = is an object that sit front of attribute and allow us to set and get the value

class Product:
    def __init__(self, price):
        # self.__price = price
        # self.set_price(price)
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            return ValueError("price can not be negative")
        self.__price = value

    # price = property(get_price , set_price)  #we use property decorator

    # product = Product(10)

    # decorator convert indtance method to class method
#  product = Product(-10)

#  print(product.price)
