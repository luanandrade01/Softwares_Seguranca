import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes de IP EXTERNO\n')
print('IP: {4}\n Região: {1}\n Pais: {2}\n Cidade: {3}\n Organização: {0}\n'.format(org,regiao,pais,cidade,ip))