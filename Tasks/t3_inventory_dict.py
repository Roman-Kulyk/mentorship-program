inventory = {
    1001: {'name': 'T-shirt', 'type': 'cloth', 'price': 15.99, 'quantity': 50},
    1002: {'name': 'Jeans', 'type': 'cloth', 'price': 29.99, 'quantity': 30},
    1003: {'name': 'Sneakers', 'type': 'footwear', 'price': 49.99, 'quantity': 20},
    1004: {'name': 'Socks', 'type': 'cloth', 'price': 9.99, 'quantity': 120},
    1005: {'name': 'Shoes', 'type': 'footwear', 'price': 79.99, 'quantity': 23}
}


def find_most_expensive_product():
    """This function prints information about the most expensive product in the
    inventory.
    """
    prices = []
    for k, v in inventory.items():
        if inventory[k]['price']:
            prices.append(inventory[k]['price'])
    max_price = max(prices)
    if inventory[k]['price'] == max_price:
        print('The most expensive product is:')
        print(v)
    # Why this solution doesn't work with min?


def find_cheapest_product():
    """This function prints information about the cheapest product in the
    inventory.
    """
    prices = []
    for k, v in inventory.items():
        if inventory[k]['price']:
            prices.append(inventory[k]['price'])
    min_price = min(prices)
    print('The cheapest price of products is:', min_price)


def find_products_by_type(type):
    """This function takes a product type as an argument and prints all product
    of that type.
    """
    products = []
    for k, v in inventory.items():
        if inventory[k]['type'] == type:
            products.append(inventory[k]['name'])
    print(products)


def calculate_total_quantity():
    """This function calculates the total quantity of all products in the
    inventory.
    """
    quantity = []
    for k, v in inventory.items():
        if inventory[k]['quantity']:
            quantity.append(inventory[k]['quantity'])
    total_quantity = sum(quantity)
    print('Total quantity of products is:', total_quantity)


def calculate_total_price():
    """This function calculates the total price of all products in the
    inventory.
    """
    prices = []
    for k, v in inventory.items():
        if inventory[k]['price']:
            prices.append(inventory[k]['price'])
    total_prices = sum(prices)
    print('Total price of products is:', total_prices)


find_most_expensive_product()
find_cheapest_product()
find_products_by_type('cloth')
print()
find_products_by_type('footwear')
print()
calculate_total_quantity()
calculate_total_price()
