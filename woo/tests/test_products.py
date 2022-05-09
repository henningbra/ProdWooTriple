import unittest
from woo.tests.wooproduct_fixture import response_simple_product
from woo.product import Product


sample_simple_product = dict(
    sku = '183504',
    name = '3M 18350 Clean & Strip rondell',
    gtin = '3004801183504',
    price = 79.0,
    regular_price = 99.0,
    sale_price = 79.0,
    standard_price = 99.0,
    manage_stock = False,
    )


class TestWooSimpleProduct(unittest.TestCase):

    def setUp(self):
        self.p = Product(**response_simple_product)

    def test_product_sku(self):
        assert self.p.sku == sample_simple_product.get('sku')

    def test_product_name(self):
        assert self.p.name == sample_simple_product.get('name')

    def test_product_price(self):
        assert self.p.price == sample_simple_product.get('price')
    
    def test_product_regular_price(self):
        assert self.p.regular_price == sample_simple_product.get('regular_price')

    def test_product_sale_price(self):
        assert self.p.sale_price == sample_simple_product.get('sale_price')

    def test_product_standard_price(self):
        assert self.p.standard_price == sample_simple_product.get('standard_price')

    def test_product_manage_stock(self):
        assert self.p.manage_stock == sample_simple_product.get('manage_stock')

    def test_product_gtin(self):
        assert self.p.gtin == sample_simple_product.get('gtin')

    def test_valid(self):
        assert self.p.valid() == True
