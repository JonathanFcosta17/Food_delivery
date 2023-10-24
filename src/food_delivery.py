class FoodDeliverySystem:
    order_id = 0

    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350,
            "Steak": 400,
            "Fish and Chips": 280,
            "Chicken Alfredo": 220,
            "Milkshake": 160
        }
        self.bill_amount = 0
        self.orders_log = {}

    def display_menu(self):
        formatted_menu = "Menu\n"
        for item, price in self.menu.items():
            formatted_menu += f"{item:<20} | {price}\n"

        return formatted_menu

    def place_order(self, customer_name, order_items):
        if all(item in self.menu for item in order_items.keys()):
            FoodDeliverySystem.order_id += 1
            order_id = FoodDeliverySystem.order_id
            order_details = {
                "customer_name": customer_name,
                "order_items": order_items,
                "status": "Placed"
            }
            self.orders_log[order_id] = order_details
            return {order_id: order_details}
        else:
            return "Order placement failed"

    def pickup_order(self, order_id):
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Picked Up"
            return "Picked Up"

        return "Order not found or already picked up"

    def deliver_order(self, order_id):
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Picked Up":
            self.orders_log[order_id]["status"] = "Delivered"
            return "Delivered"
        else:
            return "Order not found or not yet picked up"

    def modify_order(self, order_id, new_items):
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":
            for item, quantity in new_items.items():
                if item in self.menu:
                    self.orders_log[order_id]["order_items"][item] = quantity
            return self.orders_log[order_id]
        else:
            return "Order not found or already picked up"

    def generate_bill(self, order_id):
        if order_id in self.orders_log:
            total_price = sum(self.menu[item] * quantity for item,
                              quantity in self.orders_log[order_id]["order_items"].items())
            if total_price > 1000:
                total_bill_amount = total_price + 0.10 * total_price
            else:
                total_bill_amount = total_price + 0.05 * total_price
            return total_bill_amount
        else:
            return "Order not found"

    def cancel_order(self, order_id):
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":
            del self.orders_log[order_id]
            return self.orders_log
        else:
            return "Order not found or already picked up"
