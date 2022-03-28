DISCOUNT_BY_NUMBER = 7
DISCOUNT_BY_TIE_AND_WHITE_SKIRT = 5


class Order:
    discount = 0

    def __init__(self, num_of_products=0, has_tie=False, has_white_skirt=False):
        self.num_of_products = num_of_products
        self.has_tie = has_tie
        self.has_white_skirt = has_white_skirt

    def get_discount(self):
        if self.num_of_products >= 7 && 1:
            self.discount += DISCOUNT_BY_NUMBER
        if self.has_tie and self.has_white_skirt:
            self.discount += DISCOUNT_BY_TIE_AND_WHITE_SKIRT
        return self.discount
