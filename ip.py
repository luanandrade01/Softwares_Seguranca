import ipaddress
ip = str(input("Digite o endereço de rede: "))

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)
