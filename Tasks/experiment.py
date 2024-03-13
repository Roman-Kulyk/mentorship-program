inventory = {
    1001: {'name': 'T-shirt', 'type': 'cloth', 'price': 15.99, 'quantity': 50},
    1002: {'name': 'Jeans', 'type': 'cloth', 'price': 29.99, 'quantity': 30},
    1003: {'name': 'Sneakers', 'type': 'footwear', 'price': 49.99, 'quantity': 20},
    1004: {'name': 'Socks', 'type': 'cloth', 'price': 9.99, 'quantity': 120},
    1005: {'name': 'Shoes', 'type': 'footwear', 'price': 79.99, 'quantity': 23}
}




def find_cheapest_product():
    """This function prints information about the cheapest product in the
    inventory.
    """
    prices = []
    for k, v in inventory.items():
        if inventory[k]['price']:
            prices.append(inventory[k]['price'])
        curr_min_price = prices[0]
        for price in prices:
            if price < curr_min_price:
                curr_min_price = price
                if inventory[k]['price'] == curr_min_price:
                    print('The cheapest product is:')
                    print(v)
        

find_cheapest_product()