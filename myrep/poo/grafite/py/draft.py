class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.__tamanho = tamanho

    def get_calibre(self):
        return self.__calibre

    def get_dureza(self):
        return self.__dureza

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, valor: int):
        self.__tamanho = valor

    def gasto_por_folha(self):
        gastos = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return gastos.get(self.__dureza, 0)

    def __str__(self):
        return f"{self.__calibre:.1f}:{self.__dureza}:{self.__tamanho}"


class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__grafite = None

    def get_calibre(self):
        return self.__calibre

    def tem_grafite(self):
        return self.__grafite is not None

    def inserir(self, grafite: Grafite):
        if grafite.get_calibre() != self.__calibre:
            print("fail: calibre incompativel")
            return
        if self.tem_grafite():
            print("fail: ja existe grafite")
            return
        self.__grafite = grafite

    def remover(self):
        if not self.tem_grafite():
            print("fail: nao existe grafite")
            return None
        grafite_removido = self.__grafite
        self.__grafite = None
        return grafite_removido

    def escrever(self):
        if not self.tem_grafite():
            print("fail: nao existe grafite")
            return

        grafite = self.__grafite
        tamanho = grafite.get_tamanho()

        if tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = grafite.gasto_por_folha()
        tamanho_final = tamanho - gasto

        if tamanho_final < 10:
            grafite.set_tamanho(10)
            print("fail: folha incompleta")
            return

        grafite.set_tamanho(tamanho_final)

    def __str__(self):
        if self.tem_grafite():
            return f"calibre: {self.__calibre:.1f}, grafite: [{self.__grafite}]"
        else:
            return f"calibre: {self.__calibre:.1f}, grafite: null"

def main():
    lapiseira = None

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)

        elif args[0] == "show":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
            else:
                print(lapiseira)

        elif args[0] == "insert":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
                continue

            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(calibre, dureza, tamanho)
            lapiseira.inserir(grafite)

        elif args[0] == "remove":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
                continue
            lapiseira.remover()

        elif args[0] == "write":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
                continue
            lapiseira.escrever()

        else:
            print("fail: comando invalido")
main()




