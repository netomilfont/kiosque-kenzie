from menu import products


def calculate_tab(consum: list):
    consum_table = 0
    for product in products:
        for product_consum in consum:
            if product["_id"] == product_consum["_id"]:
                consum_table = product_consum["amount"] * product["price"] + consum_table
    consum_total = round(consum_table, 2)
    return {'subtotal': f'${consum_total}'}
