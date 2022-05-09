from woo.product import Product


class TripletexImportProduct:

    def __init__(self, product: Product) -> None:
        self.produktnavn = product.name
        self.produktnummer = product.sku
        self.enhet = 'Stykk'
        self.inaktiv = None
        self.innkjøpspris = None
        self.valuta = None
        self.enhetspris_eks = None
        self.enhetspris_inkl = product.standard_price
        self.mva_kode = 3
        self.produkt_for_videresalg = None
        self.regnskapskonto = None
        self.tom = None
        self.kommentar = None
        self.lagernummer = None
        self.antall = None
        self.ean_gtin = product.gtin

    def get_dict(self) -> dict:
        return vars(self)

if __name__ == "__main__":
    data = Product()
    obj = TripletexImportProduct(data)
    print(vars(obj))
    print(obj.get_dict())