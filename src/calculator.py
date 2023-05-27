class Calculator():
    def __init__(self, total_scraps, preferment_weight, scrap_dough_weight):
        self.total_scraps = total_scraps
        self.preferment_weight = preferment_weight
        self.scrap_dough_weight = scrap_dough_weight
        self.laminated_orders = []
        self.laminated_scrap_orders = []
        self.end_of_day_scrap_orders = []
    
    def add_laminated_orders(self, orders):
        for product in orders:
            self.laminated_orders.append(product)

    def add_end_of_day_scrap_orders(self, orders):
        for product in orders:
            self.end_of_day_scrap_orders.append(product)

    def add_laminated_scrap_orders(self, orders):
        for product in orders:
            self.laminated_scrap_orders.append(product)
    
    def calculate_dough(self):
        total = 0
        for product in self.laminated_orders:
            if product.order_quantity > product.frozen_quantity:
                total += ((product.order_quantity - product.frozen_quantity)//product.yeild)+1
        return total

    def laminated_scrap_product(self):
        total = self.total_scraps
        for product in self.laminated_orders:
            if product.order_quantity > product.frozen_quantity:
                total -= product.minimum_weight
        
    def available_scrap_doughs(self):
        total = self.total_scraps
        for product in self.end_of_day_scrap_orders:
            total -= (product.weight * product.order_quantity)
        for product in self.laminated_scrap_orders:
            if product.order_quantity > product.frozen_quantity:
                total -= product.minimum_weight
        if total // self.scrap_dough_weight >= 0: 
            return total // self.scrap_dough_weight
        else: 
            return 0
        
   

