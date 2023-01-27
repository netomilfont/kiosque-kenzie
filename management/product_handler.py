from menu import products

def get_product_by_id(id):
    for index, product in enumerate(products):
        if product["_id"] == id:
            return products[index]
    return {}


def get_products_by_type(type):
    product_type = []
    for index, product in enumerate(products):
        if product["type"] == type:
            product_type.append(products[index])
    return product_type