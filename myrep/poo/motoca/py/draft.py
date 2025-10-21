class Pessoa: 
    def __init__(self, nome: str,idade:int):
        self.__nome = nome 
        self.__idade = idade
        
    def __str__(self):
        return f"({self.__nome}:{self.__idade})"
    
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
        
class Moto:
    def __init__(self, potencia: int = 1):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa: Pessoa | None = None
        
    def __str__(self):
        reserva = f"power:{self.potencia}, time:{self.tempo}, person:"
        if self.pessoa == None:
            reserva += ("(empty)")
        else:
            reserva += F"({self.pessoa.get_nome()}:{self.pessoa.get_idade()})"
        return (reserva)
        
    def inserir(self, pessoa:Pessoa):
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return
        self.pessoa= pessoa
        
    def remover(self):
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        print(f"{self.pessoa.get_nome()}:{self.pessoa.get_idade()}")
        self.pessoa = None
        
    def comprarTempo(self, value: int):
        self.tempo += value
        
    def dirigir(self, tempo: int):
        if self.tempo == 0:
            print("fail: buy time first")
            return
        if self.pessoa == None:
            print("fail: empty motorcycle")
            return
        if self.pessoa.get_idade()>10:
            print("fail: too old to drive")
            return
        if tempo > self.tempo:
            print(f"fail: time finished after {tempo - self.tempo} minutes")
            self.tempo = 0
        else:
            self.tempo -= tempo
            
    def buzinar(self):
        print("P" + "e" * self.potencia + "m")
        
def main():
        moto = Moto()
        while True:
            line = input()
            print(f"${line}")
            args = line.split()
            
            if args[0] == "end":
                break 
            elif args[0] == "init":
                moto = Moto(int(args[1]))
            elif args[0] == "show":
                print(moto)
            elif args [0] == "enter":
                nome = args[1]
                idade = int(args[2])
                moto.inserir(Pessoa(nome, idade))
            elif args[0] == "leave":
                moto.remover()
            elif args[0] == "buy":
                moto.comprarTempo(int(args[1]))
            elif args[0] == "drive":
                moto.dirigir(int(args[1]))
            elif args [0] == "honk":
                moto.buzinar()
                
main()
                
                