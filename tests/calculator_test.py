import unittest
from src.calculator import Calculator
from src.laminated_product import LaminatedProduct
from src.end_of_day_scrap_product import EndOfDayScrapProduct

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(2000, 240, 1800)
        self.pan_suisse = LaminatedProduct("Pan Suisse", 10, 8, 22, True, False)
        self.ham_cheese = LaminatedProduct("Ham & Cheese", 20, 3, 22, True, False)
        self.lemon_bun = EndOfDayScrapProduct("Lemon Bun", 10, 110)
        self.laminated_orders = [self.pan_suisse, self.ham_cheese]
        self.end_of_day_scrap_orders = [self.lemon_bun]

    def test_add_orders(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.assertEqual(2, len(self.calculator.laminated_orders))
    
    def test_calculate_order_total(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.assertEqual(30, self.calculator.calculate_order_total())

    # def test_calculate_dough(self):
    #     self.calculator.add_orders(self.laminated_orders)
    #     self.assertEqual(1, self.calculator.calculate_dough())

    def test_subtract_scrap_doughs(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.assertEqual(1, self.calculator.subtract_scrap_doughs(self.calculator.calculate_dough()))