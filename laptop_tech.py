from tech_product import Tech


class Laptop(Tech):
    def __init__(self, name, price, weight, color, ram, cpu, storage):
        super().__init__(name, price, weight, color)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
    

    def set_double_price(self):
        self.price = self.price * 2
    
    def change_specs(self, ram, storage):
        if self.ram < ram or self.storage < storage:
            self.price = self.price + 1000
        self.ram = ram
        self.storage = storage
    def __str__(self):
        return f"Name : {self.name}\nPrice : {self.price} \n Weight : {self.weight}\n "\
            f"Color : {self.color} \n RAM : {self.ram}\n CPU : {self.cpu}\n"\
                f"Storage : {self.storage}\n\n"