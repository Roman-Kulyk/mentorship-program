import yaml


def print_devices_addresses_list():
    """This is a function that prints list of all devices ip_addresses in the
    file.
    """
    with open('network.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        devices = data['network']['devices']
        devices_addresses = []

        for device in devices:
            device_address = device['ip_address']
            if device_address not in devices_addresses:
                devices_addresses.append(device_address)
        print(f"Devices IP addresse are:{devices_addresses}")


def print_routers_addresses_list():
    """This is a function that prints list of all routers ip_addresses in the
     file.
     """
    with open('network.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        routers = data['network']['routers']
        routers_addresses = []

        for router in routers:
            router_address = router['ip_address']
            if router_address not in routers_addresses:
                routers_addresses.append(router_address)
        print(f"Routers IP address are:{routers_addresses}")


def print_routers_interfaces_list():
    """This is a function that prints list of all routers' interfaces
     ip_addresses in the file.
     """
    with open('network.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        routers = data['network']['routers']
        routers_interfaces = []

        for router in routers:
            router_interface = router['interfaces'][0]['ip_address']
            if router_interface not in routers_interfaces:
                routers_interfaces.append(router_interface)
        print(f"Routers interfaces ip address are:{routers_interfaces}")


print_devices_addresses_list()
print()
print_routers_addresses_list()
print()
print_routers_interfaces_list()
