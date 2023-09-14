import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_returns_0_when_called_with_1_items(self):
        prices = [23]
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_list_of_two_prices(self):
        prices = [30, 43]
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_four_items(self):
        prices = [11, 3, 6, 7]
        expected_discount = 3
        self.assertEqual(expected_discount, discount(prices))


    def test_if_list_empty(self):
        prices = []
        expected_discount = 0  # No items, so no discount
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_price(self):
        prices = [15]
        expected_discount = 0  # Only one item, so no discount
        self.assertEqual(expected_discount, discount(prices))

    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()