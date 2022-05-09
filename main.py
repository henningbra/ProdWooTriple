import settings
from woocommerce import API
from woo.product import Product
from triple.product import TripletexImportProduct
from triple.export import ExcelWriter

wcapi = API(
    url=settings.WOOCOMMERCE_URL,
    consumer_key=settings.WOOCOMMERCE_CONSUMER_KEY,
    consumer_secret=settings.WOOCOMMERCE_CONSUMER_SECRET,
    version="wc/v3"
)

def get_products():
    page = 1
    data = True
    product_list = list()
    while data:
        params={'per_page': 100, 'page': page}
        response = wcapi.get("products", params=params)
        data = response.json()
        for item in data:
            p = Product(**item)
            if p.valid():
                product_list.append(p)
            if p.variations:
                for variation in p.variations:
                    variation_response = wcapi.get(f'products/{variation}')
                    variation_data = variation_response.json()
                    p = Product(**variation_data)
                    if p.valid():
                        product_list.append(p)
        data = response.json()
        page += 1
    return product_list
    
def get_product(id):
    return wcapi.get(f'products/{id}')

def export_excel():
    product_list = get_products()
    data = list()
    for product in product_list:
        triple_product = TripletexImportProduct(product)
        data.append(triple_product.get_dict())
    writer = ExcelWriter(data)
    writer.save(filename='product_export.xlsx')

if __name__ == "__main__":
    # data = get_products()
    print(export_excel())