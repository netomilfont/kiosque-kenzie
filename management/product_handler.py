from statistics import mode
from menu import products

def get_product_by_id(id: int):
    if type(id) == int:
        for product in products:
            if product["_id"] == id:
                return product
        return {}
    else:
        raise TypeError("product id must be an int")


def get_products_by_type(type_product: str):
    if type(type_product) == str:
        product_type_list = []
        for product in products:
            if product["type"] == type_product:
                product_type_list.append(product)
        return product_type_list
    else:
        raise TypeError("product type must be a str")

def add_product(menu: list, **new_product: dict):
    product_id = 0
    for product in menu:
        if product["_id"] > product_id:
            product_id = product["_id"]
    new_product["_id"] = product_id + 1
    menu.append(new_product)
    return new_product


def menu_report():
    count_products = 0
    price_total = 0
    list_type = []

    for product in products:
        count_products = count_products + 1
        price_total = price_total + product["price"]
        list_type.append(product["type"])

    most_common = mode(list_type)
    average_price = price_total / count_products
    
    return f'Products Count: {count_products} - Average Price: ${round(average_price, 2)} - Most Common Type: {most_common}'