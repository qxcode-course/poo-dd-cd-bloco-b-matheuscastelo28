class Pessoa: 
    def __init__(self, nome: str,idade:int):
        self.__nome = nome 
        self.__idade = idade
        
    def __str__(self):
        return f"({self.__nome}:{self.__idade})"
    
    def getnome(self):
        return self.__nome
    
    def getidade(self):
        return self.__idade
        
class Moto:
    def __init__(self, potencia: int = 1):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa: Pessoa | None = None
        
    def __str__(self):
        