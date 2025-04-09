def numero():
    n = int(input("Digite um número: "))
    return n
print("Escolha o tipo de conversão (decimal para...)\nDigite: ")
tipo = int(input("1 -> Binário\n2 -> Hexadecimal\n3 -> Octal\n4 -> ENCERRAR\n"))
while tipo != 4 :
    if tipo == 1:
        n = numero()
        # Base 2(binary)
        bin_n = str(bin(n))
        bin_n_format = bin_n.replace(bin_n[1],"")
        print("="*50)
        print(bin_n_format)
        print("="*50)
    elif tipo == 2:
        n = numero()
        # Base 16(hexadecimal)
        hex_n = hex(n)
        print("="*50)
        print(hex_n)
        print("="*50)
    elif tipo == 3:
        n = numero()
        # Base 8(octal)
        oct_n = oct(n)
        print("="*50)
        print(oct_n)
        print("="*50)
    else:
        print("Digite uma das alternativas abaixo")
    tipo = int(input("1 -> Binário\n2 -> Hexadecimal\n3 -> Octal\n4 -> ENCERRAR\n"))

