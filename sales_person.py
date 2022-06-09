class SalePerson:
    employee_id = 0
    def __init__(self, first_name, last_name, salary, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        SalePerson.employee_id += 1
        self.salary = salary
        self.date_joined = date_joined
        self.product_sold = []
        self.total_sales = 0

    
    def sell_product(self, product):
        print(f"Selling {product.name}")
        self.product_sold.append(product)
    
    
    def display_sales(self):
        print("-----------------------------------------")
        print("Product Sold: ")
        for product in self.product_sold:
            print(product)
        print("-----------------------------------------")
    
    
    def calculate_sales(self):
        total = 0
        for product in self.product_sold:
            total += product.price
        self.total_sales = total
        return total
        
    
    def calculate_commission(self, percentage):
        total = self.calculate_sales()
        return f"Commission :{total * percentage}"
    
    
    def total_product_sold(self):
        return f"The number of products sold : {len(self.product_sold)}"
    
   
    def sort_by_price(self):
        self.product_sold.sort(key=lambda product: product.price, reverse=True)