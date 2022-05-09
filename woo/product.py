import html

VARIANT = 'variable'
INVALID_PRODUCTS = ['variable',]

class Product:

    def __init__(self, id, sku, **kwargs) -> None:
        self.id = id
        self.sku = sku
        self.name = html.unescape(kwargs.get('name'))
        self.regular_price = self.string_to_float(kwargs.get('regular_price'))
        self.sale_price = self.string_to_float(kwargs.get('sale_price'))
        self.on_sale = kwargs.get('on_sale')
        self.price = self.string_to_float(kwargs.get('price'))
        self.manage_stock = kwargs.get('manage_stock')
        self.type = kwargs.get('type')
        self.parent_id = kwargs.get('parent_id')
        self.gtin = self._extract_meta_gtin(kwargs.get('meta_data'))
        self.variations = kwargs.get('variations', None)

    def _extract_meta_gtin(self, meta_data) -> str:
        for meta in meta_data:
            if meta['key'] == '_woosea_gtin':
                return meta['value']

    @property
    def standard_price(self):
        """ Output the standard list price """
        return self.regular_price if (self.regular_price and self.on_sale) else self.price

    def variant(self):
        """ Check if product is variant"""
        status = False
        if self.type == VARIANT: 
            return True
        else:
            return False

    def valid(self):
        """ Check if product ready for export  """
        status = True
        if not self.sku: 
            status = False
        if self.type in INVALID_PRODUCTS: 
            status = False
        return status

    @staticmethod
    def string_to_float(string: str) -> float:
        return float(string) if string else float(0)

    def __str__(self):
        status = '[OK]' if self.valid() else '[IGNORED]'
        return f'Product:{self.sku.ljust(8)} {self.name[:20].ljust(20)} price:{self.standard_price:06.1f}  {status}'