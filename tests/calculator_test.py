import unittest
from src.calculator import Calculator
from src.laminated_product import LaminatedProduct
from src.laminated_scrap_product import LaminatedScrapProduct
from src.end_of_day_scrap_product import EndOfDayScrapProduct

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(8000, 240, 1800)
        self.pan_suisse = LaminatedProduct("Pan Suisse", 10, 8, 22, True, True)
        self.ham_cheese = LaminatedProduct("Ham & Cheese", 10, 3, 22, True, True)
        self.lemon_bun = EndOfDayScrapProduct("Lemon Bun", 15, 110)
        self.custard_bun = EndOfDayScrapProduct("Custard Bun", 2, 110)
        self.morning_bun = LaminatedScrapProduct("Morning Bun", 23, 22, 4000)
        self.laminated_orders = [self.pan_suisse, self.ham_cheese]
        self.laminated_scrap_orders = [self.morning_bun]
        self.end_of_day_scrap_orders = [self.lemon_bun, self.custard_bun]

    def test_add_orders(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.assertEqual(2, len(self.calculator.laminated_orders))

    def test_add_end_of_day_scrap_orders(self):
        self.calculator.add_end_of_day_scrap_orders(self.end_of_day_scrap_orders)
        self.assertEqual(2, len(self.calculator.end_of_day_scrap_orders))

    def test_add_laminated_scrap_orders(self):
        self.calculator.add_laminated_scrap_orders(self.laminated_scrap_orders)
        self.assertEqual(1, len(self.calculator.laminated_scrap_orders))

    def test_calculate_dough(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.assertEqual(2, self.calculator.calculate_dough())

    def test_available_scrap_doughs(self):
        self.calculator.add_laminated_orders(self.laminated_orders)
        self.calculator.add_end_of_day_scrap_orders(self.end_of_day_scrap_orders)
        self.calculator.add_laminated_scrap_orders(self.laminated_scrap_orders)
        self.assertEqual(1, self.calculator.available_scrap_doughs())
