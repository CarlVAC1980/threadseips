import ipaddress

ip = '192.168.0.0/32'

rede = ipaddress.ip_network(ip, strict=False)

#print(rede)
for ip in rede:
    print(ip)


