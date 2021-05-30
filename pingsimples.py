import os

print("-" * 42)
print('''TESTANDO CONECTIVIDADE ENTRE DISPOSITIVOS ''')
print("-" * 42)

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

os.system(f'ping -n 6 {ip_ou_host}')