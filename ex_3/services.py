from .models import Order


class OrderService:
    def get_order_discount(self, order: Order) -> int:
        return order.get_discount()
