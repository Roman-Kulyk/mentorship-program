# with open('network.yaml') as f:
#     data = f.read()
#     print(data)

import yaml
def print_ip_address_list():
    """This is a function that prints list of all ip_addresses in the file."""
    pass
    with open('network.yaml', 'r') as file:
        service = yaml.safe_load(file)
        print(service['network']['routers'][0]['ip_address'])
        #print(service)
print_ip_address_list()