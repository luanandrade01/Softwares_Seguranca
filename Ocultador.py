import ctypes

pasta = input("Digite a pasta que quer ocultar: ")

atributo_ocultar = 0x02


retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)


if retorno:
    print("Arquivo Ocultado")
else:
    print("Arquivo não foi ocultado")