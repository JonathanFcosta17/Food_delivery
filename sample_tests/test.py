import unittest
from src.food_delivery import FoodDeliverySystem


class Test(unittest.TestCase):
    def test_validation(self):
        f = FoodDeliverySystem()
        expected_menu = """
            Menu
            Burger               | 150
            Pizza                | 250
            Pasta                | 200
            Salad                | 120
            Beverages            | 130
            Noodles              | 150
            Sushi                | 270
            Bakery               | 350
            Steak                | 400
            Fish and Chips       | 280
            Chicken Alfredo      | 220
            Milkshake            | 160
        """

        actual_menu = f.display_menu()

        # Split the strings into lines
        expected_lines = expected_menu.strip().split('\n')
        actual_lines = actual_menu.strip().split('\n')

        # Compare each line
        for expected_line, actual_line in zip(expected_lines, actual_lines):
            self.assertEqual(actual_line.strip(), expected_line.strip())

    def test_validation1(self):
        f = FoodDeliverySystem()
        order = f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2})
        order_id = list(order.keys())[0]  # Extract the generated order_id
        self.assertEqual(order, {
            order_id: {"customer_name": "Mary Smith", "order_items": {
                "Burger": 1, "Pasta": 2}, "status": "Placed"}
        })

    def test_validation2(self):
        f = FoodDeliverySystem()
        order = f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2})
        order_id = list(order.keys())[0]  # Extract the generated order_id
        bill_amount = f.generate_bill(order_id)
        self.assertEqual(bill_amount, 577.5)

    def test_validation3(self):
        f = FoodDeliverySystem()
        order = f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2})
        order_id = list(order.keys())[0]  # Extract the generated order_id
        pickup_status = f.pickup_order(order_id)
        expected_status = "Picked Up"
        self.assertEqual(pickup_status, expected_status)

    def test_validation4(self):
        f = FoodDeliverySystem()
        order = f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2})
        order_id = list(order.keys())[0]  # Extract the generated order_id
        f.pickup_order(order_id)  # Pick up the order
        delivery_status = f.deliver_order(order_id)
        self.assertEqual(delivery_status, "Delivered")


if __name__ == '__main__':
    unittest.main()
