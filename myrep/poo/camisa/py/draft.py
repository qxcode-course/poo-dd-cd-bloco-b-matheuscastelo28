class Camiseta:
    def __init__(self):
        self._tamanho = ""
        
    def getTamanho(self):
        return self._tamanho
        
    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M",  "G", "GG", "XG"]
        valor = valor.upper()
        valor = tamanhos_validos
        if valor in tamanhos_validos:
            self._tamanho = valor 
        else:
            print(" Esse tamanho não é permitido, os tamanhos validos são PP, P, M, G, GG, XG")
            
def main(): 
    roupa = Camiseta()
    while True:
        line = input()
        args = line.split()
        print(f"${line}")
        
        if args[0] == "end":
            break
        elif args[0] == "init":
            roupa = Camiseta()
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            
            roupa.setTamanho(args[1])
main()