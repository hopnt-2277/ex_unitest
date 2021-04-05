import unittest
from ex_3.services import OrderService
from ex_3.models import Order, DISCOUNT_BY_NUMBER, DISCOUNT_BY_TIE_AND_WHITE_SKIRT


class OrderTest(unittest.TestCase):
    service = OrderService()

    def test_something(self):
        self.assertEqual(True, True)

    def test_blank_order(self):
        order = Order()
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, 0)

    def test_order_with_only_discount_by_number(self):
        order = Order(num_of_products=7)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, DISCOUNT_BY_NUMBER)

    def test_order_with_discount_by_number_and_products(self):
        order = Order(num_of_products=7, has_tie=True, has_white_skirt=True)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, DISCOUNT_BY_NUMBER + DISCOUNT_BY_TIE_AND_WHITE_SKIRT)

    def test_order_with_discount_not_enough_number_and_products(self):
        order = Order(num_of_products=6, has_tie=True, has_white_skirt=True)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, DISCOUNT_BY_TIE_AND_WHITE_SKIRT)

    def test_order_with_discount_by_number_and_only_has_tie(self):
        order = Order(num_of_products=7, has_tie=True)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, DISCOUNT_BY_NUMBER)

    def test_order_with_discount_not_enough_number_and_only_has_tie(self):
        order = Order(num_of_products=6, has_tie=True)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, 0)

    def test_order_with_discount_by_number_and_has_none_tie(self):
        order = Order(num_of_products=7, has_tie=False)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, DISCOUNT_BY_NUMBER)

    def test_order_with_discount_not_enough_number_and_has_none_tie(self):
        order = Order(num_of_products=6)
        discount = self.service.get_order_discount(order)
        self.assertEqual(discount, 0)
