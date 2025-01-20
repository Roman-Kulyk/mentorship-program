inventory = {
    1001: {'name': 'T-shirt', 'type': 'cloth', 'price': 15.99, 'quantity': 50},
    1002: {'name': 'Jeans', 'type': 'cloth', 'price': 29.99, 'quantity': 30},
    1003: {'name': 'Sneakers', 'type': 'footwear', 'price': 49.99, 'quantity': 20},
    1004: {'name': 'Socks', 'type': 'cloth', 'price': 9.99, 'quantity': 120},
    1005: {'name': 'Shoes', 'type': 'footwear', 'price': 79.99, 'quantity': 23}
}


def most_expensive_product():
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


def cheapest_product():
    """This function prints information about the cheapest product in the
    inventory.
    """
    prices = []
    # for k, v in inventory.items():
    #     if inventory[k]['price']:
    #         prices.append(inventory[k]['price'])
    #     curr_min_price = prices[0]
    #     for price in prices:
    #         if price < curr_min_price:
    #             curr_min_price = price
    #             if inventory[k]['price'] == curr_min_price:
    #                 print('The cheapest product is:')
    #                 print(v)

    ##### 2 #####
    # for id, item_data in inventory.items():
    #     if inventory[id]['price']:
    #         prices.append(inventory[id]['price'])
    
    # current_min_price = min(prices)

    # for id, item_data in inventory.items():
    #     if inventory[id]['price'] == current_min_price:
    #         print(f"The cheapest product is: {item_data}")

    ##### 3 #####
    item = 0
    for id, item_data in inventory.items():
        current_price = inventory[id]['price']
        if item == 0:
            item = item_data
        else:
            if current_price < item_data['price']:
                item = item_data
    print(f"The cheapest product is: {item}")


def products_by_type(type):
    """This function takes a product type as an argument and prints all product
    of that type.
    """
    products = []
    for k, v in inventory.items():
        if inventory[k]['type'] == type:
            products.append(inventory[k]['name'])
    print(products)


def total_quantity():
    """This function calculates the total quantity of all products in the
    inventory.
    """
    quantity = []
    for k, v in inventory.items():
        if inventory[k]['quantity']:
            quantity.append(inventory[k]['quantity'])
    total_quantity = sum(quantity)
    print('Total quantity of products is:', total_quantity)


def total_price():
    """This function calculates the total price of all products in the
    inventory.
    """
    prices = []
    for k, v in inventory.items():
        if inventory[k]['price']:
            prices.append(inventory[k]['price'])
    total_prices = sum(prices)
    print('Total price of products is:', total_prices)


commands_list = ['most_expensive_product', 
                 'cheapest_product',
                 'total_quantity', 
                 'total_price', 
                 'exit']
while True:
    print('This program is intended to manage your inventory. Available commands:')
    print(commands_list)
    # command = input("Enter your command: ")
    # if command == 'most_expensive_product':
    #     most_expensive_product()
    # elif command == 'cheapest_product':
    #     cheapest_product()
    # elif command == 'total_quantity':
    #     total_quantity()
    # elif command == 'total_price':
    #     total_price()
    # elif command == 'exit':
    #     break
    command = input("Enter your command: ")
    match command:
        case 'most_expensive_product':
            most_expensive_product()
        case 'cheapest_product':
            cheapest_product()
        case 'total_quantity':
            total_quantity()
        case 'total_price':
            total_price()
        case 'exit':
            break
        case _:
            print("It seem's that you entered not correct command.")
