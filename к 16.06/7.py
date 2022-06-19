f = open('26.txt')
N = int(f.readline())
#255.255.224.0
requests = {}
for _ in range(N):
    address = f.readline().split()
    address_user = '.'.join(address)
    address_network = '.'.join([address[0], address[1], str(224 & int(address[2])), '0'])
    if address_network not in requests:
        requests[address_network] = dict()
        requests[address_network]['count_requests'] = 1
        requests[address_network]['requests'] = {address_user}
    else:
        requests[address_network]['count_requests'] += 1
        requests[address_network]['requests'].add(address_user)
max_requests = 0
max_address = ''
for network in requests:
    if requests[network]['count_requests'] > max_requests:
        max_requests = requests[network]['count_requests']
        max_address = network
    elif requests[network]['count_requests'] == max_requests:
        if len(requests[network]['requests']) > len(requests[network]['requests']):
            max_address = network
        elif len(requests[network]['requests']) == len(requests[network]['requests']):
            address1 = sum([int(i) for i in max_address.split('.')])
            address2 = sum([int(i) for i in network.split('.')])
            if address2 > address1:
                max_address = network
print(max_address, len(requests[max_address]['requests']))
