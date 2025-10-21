# código do Tempo
# 1. usar o __ no começo pra definir private
# 2. criar um get_algo para leitura e retornar o valor
# 3. criar um set_algo que recebe um valor
# 4. parametros default utilizados quando o valor não vem
# 5. parametros nomeados quando quero um valor especifico

# class Tempo:
#     def __init__(self, hora: int = 0, min: int = 0):
#         self.__h = 0
#         self.set_hora(hora)
#         self.__m = min
#         self.__s = 0

#     def set_hora(self, valor: int) -> None: # escrita
#         if valor > 11 or valor < 0:
#             print("hora errada")
#             return
#         self.__h = valor

#     def get_hora(self) -> int: # leitura
#         return self.__h

#     def __str__(self): 
#         return f"{self.__h}:{self.__m}:{self.__s}"

# agora = Tempo(min=55, hora=9)
# print(agora)


# Vamos implementar uma classe que controla os possíveis valores de calçados para uma chinela.
# As regras de validação de valores são as seguintes.
# Uma chinela tem um valor tamanho que é um número par entre 20 e 50, incluindo 20 e 50.
# Faça o objeto chinela iniciar com tamanho 0 e controle através do método setTamanho que apenas valores válidos de tamanho sejam atribuídos.
# Por fim, crie um loop no qual um objeto chinela é criado e é perguntado ao usuário qual seu tamanho de chinela.
# Mantenha o usuário preso no loop até que ele insira um valor válido.
# Caso ele digite um valor inválido, avise e dê uma mensagem de erro adequada.

class Chinela:
    def __init__(self, tamanho:int):
        self.__tamanho = 0
        self.setTamanho(tamanho)
        
    
    def setTamanho(self, valor: int) -> bool:
        if valor >20 or valor <50:
            print(f" Este tamanho é invalido, deve ser um numero entre 20 e 50")
            return False
        if valor % 2 !=0:  
            print(f"fail, precisa ser um numero par")
            return False
        self.__tamanho = valor 
        return True
        
        
    def  getTamanho(self)-> int:
        return self.__tamanho

        
def main():
    chinela = Chinela()
    while True:
        numero: int = int(input("Qual o tamanho da chinela que você quer"))
        if  chinela.setTamanho(numero) == True:
            break
main()
        
        
        
            