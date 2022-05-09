from tripletex.tripletex import Tripletex
from tripletex.config import Config


config = Config()

client = Tripletex.from_config(config)

def get_product_by_id(sku):
    return client.get_product_by_id(sku)

if __name__ == "__main__":
    print(get_product_by_id(539243))