class Camisa():
    def __init__(self):
        self.__tamanho = ""

    def set_tamanho(self, tamanho:str)-> bool:
        opcoes = ['PP', 'P', 'M', 'G', 'GG', 'XG']
        if tamanho in opcoes:
            self.__tamanho = tamanho 
            self.__tamanho = tamanho
    
            return True
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG") 
            return False

    def __str__(self):
            return f"size: ({self.__tamanho})"


def main ():
    camisa = Camisa()
    while True:
        line = input()
        args = line.split()
        print(f"${line}")

        if args[0] == "end":
            break 
        elif args[0] == "init":
            camisa = Camisa()
        elif args[0] == "show":
            print(camisa)
        elif args[0] == "size":
            camisa.set_tamanho(args[1])


main()


