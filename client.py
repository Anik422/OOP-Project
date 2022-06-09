from mobile_tech import Tech
from laptop_tech import Laptop
from mobile_tech import Mobile
from sales_person import SalePerson
from datetime import date


phone_1 = Mobile("Iphone 11", 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile("Iphone 12", 70000, 550, 'Silver', '1920-1080', 12)
phone_3 = Mobile("Iphone 13", 80000, 580, 'Project Red', '1920-1080', 13)


laptop_1 = Laptop("Asus g14", 130000, 1.6, 'Moonlight Silver', 16, 'Ryzen 4800', 512)
laptop_2 = Laptop("Macbook Pro 13", 120000, 1.7, 'Dark Grey', 8, 'Intel core i5', 512)
laptop_3 = Laptop("Dell XPS 13", 140000, 1.4, 'Whit', 16, 'Intel core i7', 512)

# test methods
print(laptop_1)
print(phone_1)

# Applying the discount upon the product
phone_1.apply_discount()
print(phone_1.price)


# total number of product
print(Tech.total_number_of_products())

#shipping Cost
print(laptop_3.calculate_shipping_cost(10))

# Changing specs for laptop 3
print(laptop_3)
laptop_3.change_specs(32, 1000)
print(laptop_3)

sales_parson_1 = SalePerson("Anik", "Saha", 40000, date(2022, 1, 5))


# adding the products
sales_parson_1.sell_product(phone_1)
sales_parson_1.sell_product(phone_2)
sales_parson_1.sell_product(laptop_1)
sales_parson_1.sell_product(laptop_2)


# total products sold 
print(sales_parson_1.total_product_sold())

# products sold :
sales_parson_1.display_sales()

#calculate commission
print(sales_parson_1.calculate_commission(0.2))


#sort the sold products by price
sales_parson_1.sort_by_price()
sales_parson_1.display_sales()

# sort the sold products by price
sales_parson_1.sort_by_price()