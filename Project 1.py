from abc import ABC, abstractmethod

#------------Project class------------
class Product:
    
    # Constructor
    def __init__ (self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    # Updates Quantity   
    def update_quantity(self,new_quantity):
        self.quantity = new_quantity
        print(f"Quantity updated to : {self.quantity}\n")
        
    # Gets Product Info   
    def get_product_info(self):
        print(f"Product Id: {self.product_id}\nName: {self.name}")
        print(f"Price: ${self.price:,.2f}")
        print(f"Quantity: {self.quantity}")
 
# Testing prints

# creates object in Product class
print("\t\tPRODUCT CLASS TEST\n")
item1 = Product(id("Toy"),"Toy",12.99,1344)

# Gets product info on item1
Product.get_product_info(item1)

# updates item quantity
print("\t\tPRODUCT CLASS - UPDATE QUANTITY TEST\n")
Product.update_quantity(item1, 1000)

# Gets product info on item1
Product.get_product_info(item1)

#------------DigitalProduct class------------ 
class DigitalProduct(Product):
    
    # Constructor
    def __init__(self, product_id, name, price, quantity, file_size, download_link):
        super().__init__(product_id, name, price, quantity)

        self.file_size = file_size
        self.download_link = download_link
        
    # Gets Product Info    
    def get_pruduct_info(self):
        super().get_product_info()
    
        print(f"File Size: {self.file_size}\nDownload Link: {self.download_link}\n")

# Testing prints
print("\t\tDIGITAL PRODUCT CLASS TEST\n")

# creates object in DigitalProduct class and tests get_product_info
Ditem1 = DigitalProduct(id("Feather Hat Image"),"Feather Hat Image",99.99,231,"1.2GB", "https:freehats.org" )
DigitalProduct.get_pruduct_info(Ditem1)

# creates object in DigitalProduct class and tests get_product_info
Ditem2 = DigitalProduct(id("Waterfall Image"),"Waterfall Image",10.99,1000000,"10MB", "https:WaterfallImages.gov" )
DigitalProduct.get_pruduct_info(Ditem2)

#------------PhysicalProduct class------------
class PhysicalProduct(Product):
    
    # Constructor
    def __init__ (self, product_id, name, price, quantity, weight, dimensions, shipping_cost):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost
    
    # Gets Product Info   
    def get_pruduct_info(self):
        super().get_product_info()
        
        print(f"Weight: {self.weight}\nDimensions: {self.dimensions}\nShipping Cost: ${self.shipping_cost}\n")


# Testing prints

print("\t\tPHYSICAL PRODUCT CLASS TEST\n")

# creates object: Pitem1 in PhysicalProduct class and tests get_product_info    
Pitem1 = PhysicalProduct(id("Water Bottle"),"Water Bottle" ,1.99,1243423, "0.5 Lb" , "1x1x1 mm", "10.99")
PhysicalProduct.get_pruduct_info(Pitem1)

# creates object: Pitem2 in PhysicalProduct class and tests get_product_info
Pitem2 = PhysicalProduct(id("Computer"),"Computer" ,1499.99,300, "20 Lb" , ".5x.25x.75 m", "14.99")
PhysicalProduct.get_pruduct_info(Pitem2)

#create object: Pitem3 in PhysicalProduct class and tests get_product_info
Pitem3 = PhysicalProduct(id("Toy"),"Toy",12.99,1344,"1 Lb","1x1x1 mm","5.99")
PhysicalProduct.get_pruduct_info(Pitem3)


#------------Cart class------------
class Cart:
    
    # Constructor that defines cart items as private attribute
    def __init__ (self):
        self.___cart_items = []

    # adds product to the cart
    def add_product(self,product):
        self.___cart_items.append(product)
        print(f"{product.name} added to cart\n")
    
    # removes product from cart
    def remove_product(self,product_id):

        # searches each product to find the matching product_id in the cart
        for product in self.___cart_items:
            if product.product_id == product_id:
                self.___cart_items.remove(product)
        print(f"{product.name} removed from cart\n")

    # Views product(s) in cart
    def view_cart(self):

        # prints each product by name in the cart
        for product in self.___cart_items:
            print(f"{product.name} in cart\n")
        
    # calculates price of all products   
    def calculate_total(self):
        total = 0
        for product in self.___cart_items:
            total += product.price
        print(f"Total: ${total}\n")
        return total

    # additional method to clear cart
    def clear_cart(self):
        self.___cart_items.clear()  
    

#Testing prints
print("\t\tCART CLASS TEST\n")

#create cart as object
cart = Cart()

# add to cart
cart.add_product(Pitem1)
cart.add_product(Ditem1)

# remove from cart
cart.remove_product(Ditem1.product_id)

# view cart
cart.view_cart()

# calculate total
cart.calculate_total()

#------------User Class------------
class User:   

    # Constructor
    def __init__(self, user_id, name, cart):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()
        

    # adds item to cart
    def add_to_cart(self,product):
        self.cart.add_product(product)
            
        # removes item from cart    
    def remove_from_cart(self,product_id):
        self.cart.remove_product(product_id)
        
        # checks out the product(s)
    def checkout(self,discount=None):

        # prints user name calculates total
        print(self.name,"is checking out\n")

        # applies discount if discount is not None
        if discount:
            discount.apply_discount(self.cart.calculate_total())
        else:
            print(f"No discount applied.\nTotal: ${self.cart.calculate_total()}\n")

        #clears cart
        self.cart.clear_cart()
        
        
#Testing prints
print("\t\tUSER CLASS TEST\n")
print("\tUser1 TEST\n")

#create user as object. adds and removes Physical products to cart
User1 = User(id("John Doe"),"John Doe",cart)
User1.add_to_cart(Pitem1)
User1.remove_from_cart(Pitem1.product_id)
User1.add_to_cart(Pitem1)
User1.add_to_cart(Pitem2)

print("\tUser2 TEST\n")

#create user as object. adds and removes Digital products to cart
User2 = User(id("Jane Doe"),"Jane Doe",cart)
User2.add_to_cart(Ditem1)
User2.remove_from_cart(Ditem1.product_id)
User2.add_to_cart(Ditem1)
User2.add_to_cart(Ditem2)

#------------Discount Class------------
class Discount(ABC):
    def __init__(self,total_amount,percentage):
        self.total_amount = total_amount
        self.percentage = percentage
 
    # applies discount to total amount 
    @abstractmethod   
    def apply_discount(self,total_amount):
        pass

#tests if abstract method works (intentionally creates error)
#discount = Discount(1000,0.10)

#------------PercentageDiscount class------------
class PercentageDiscount(Discount):

    def __init__(self,total_amount, percentage):
        self.total_amount = total_amount
        self.percentage = percentage
        
    # applies discount to total amount
    def apply_discount(self,total_amount):
        print(f"Total before Percentage discount: ${total_amount:.2f}")

        discount_amount = self.total_amount * self.percentage
        total_amount = total_amount - discount_amount
        print(f"Total after Percentage discount: ${total_amount:.2f}\n")

#Testing prints
print("\t\tPERCENTAGE DISCOUNT CLASS TEST\n")

#create object in PercentageDiscount class       
discount1 = PercentageDiscount(1000, 0.10)
print("discount1 percentage:",discount1.percentage)

#tests the apply_discount method
discount1.apply_discount(1000)

#------------FixedAmountDiscount class------------ 

class FixedAmountDiscount(Discount):

    def __init__(self,amount):
        self.amount = amount
        
    # applies discount to total amount
    def apply_discount(self,total_amount):
        print(f"Total before Fixed Amount discount: ${total_amount:.2f}")

        total_amount = total_amount - self.amount
        print(f"Total after Fixed Amount discount: ${total_amount:.2f}\n")

#Testing prints
print("\t\tFIXED AMOUNT DISCOUNT CLASS TEST\n")

#create object in FixedAmountDiscount class
discount2 = FixedAmountDiscount(200)
print("discount2 amount:",discount2.amount,"\n")

#tests the apply_discount method
discount2.apply_discount(2000)

#------------Continued User Class Test------------
print("\t\tUSER CLASS TEST CONTINUED\n")

#creates discount objects (PercentageDiscount discounts total to fully test Percent discount)
Per = PercentageDiscount(User1.cart.calculate_total(), 0.10)
Fix = FixedAmountDiscount(20)

# checks out with Fix (FixedAmountDiscount Object) and Per (PercentageDiscount Object)
User1.checkout(Per)
User2.checkout(Fix)

# checks out to test id cart is empty
User1.checkout()
User2.checkout()
