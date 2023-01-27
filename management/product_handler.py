from menu import products

def get_product_by_id(id: int):
    for index, product in enumerate(products):
        if product["_id"] == id:
            return products[index]
    return {}


def get_products_by_type(type: str):
    product_type = []
    for index, product in enumerate(products):
        if product["type"] == type:
            product_type.append(products[index])
    return product_type


def add_product(menu: list, **new_product: dict):
    product_id = 0
    for product in menu:
        if product["_id"] > product_id:
            product_id = product["_id"]
    new_product["_id"] = product_id + 1
    menu.append(new_product)
    return new_product