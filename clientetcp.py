import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f'Erro: {e}')
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Porta: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Conexão aceita com sucesso!")
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível concectar no host: " + HostAlvo)
        print(f'Erro: {e}')
        sys.exit()

if __name__ == "__main__":
    main()
