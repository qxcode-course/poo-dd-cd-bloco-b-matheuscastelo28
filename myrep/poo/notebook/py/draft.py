class Notebook:
    def __init__(self):
        self.__ligado: bool = False

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("msg: notebook ligado")
        else:
            print("msg: notebook já está ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("msg: notebook desligado")
        else:
            print("msg: notebook já está desligado")

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        print(f"msg: Status: {status}")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("msg: erro: ligue o notebook primeiro")
        else:
            print(f"msg: Usando por {tempo} minutos")


# ================== PARTE 2 - Notebook com Bateria ==================

class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def get_capacidade(self):
        return self.__capacidade

    def get_carga(self):
        return self.__carga

    def descarregar(self, tempo: int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0

    def carregar(self, tempo: int):
        self.__carga += tempo
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")


class Notebook2:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is not None:
            print("msg: bateria removida")
            b = self.__bateria
            self.__bateria = None
            self.__ligado = False
            return b
        else:
            print("msg: sem bateria")
            return None

    def ligar(self):
        if self.__bateria is None or self.__bateria.get_carga() <= 0:
            print("msg: não foi possível ligar")
        else:
            self.__ligado = True
            print("msg: notebook ligado")

    def desligar(self):
        self.__ligado = False
        print("msg: notebook desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("msg: notebook desligado")
            return

        carga_atual = self.__bateria.get_carga()
        if carga_atual == 0:
            print("msg: notebook descarregado")
            self.__ligado = False
            return

        if tempo >= carga_atual:
            print(f"msg: Usando por {carga_atual} minutos, notebook descarregou")
            self.__bateria.descarregar(tempo)
            self.__ligado = False
        else:
            print(f"msg: Usando por {tempo} minutos")
            self.__bateria.descarregar(tempo)

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        if self.__bateria is None:
            print(f"msg: Status: {status}, Bateria: Nenhuma")
        else:
            print(f"msg: Status: {status}, Bateria: ({self.__bateria.get_carga()}/{self.__bateria.get_capacidade()})")


# ================== PARTE 3 - Notebook com Bateria e Carregador ==================

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")


class Notebook3:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is not None:
            print("msg: bateria removida")
            b = self.__bateria
            self.__bateria = None
            if self.__carregador is None:
                self.__ligado = False
            return b
        else:
            print("msg: sem bateria")
            return None

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador is not None:
            print("msg: carregador removido")
            self.__carregador = None
            if self.__bateria is None:
                self.__ligado = False
        else:
            print("msg: sem carregador")

    def ligar(self):
        if (self.__bateria and self.__bateria.get_carga() > 0) or self.__carregador:
            self.__ligado = True
            print("msg: notebook ligado")
        else:
            print("msg: não foi possível ligar")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("msg: notebook desligado")
            return

        # Caso 1: apenas bateria
        if self.__bateria and not self.__carregador:
            carga = self.__bateria.get_carga()
            if tempo >= carga:
                print(f"msg: Usando por {carga} minutos, notebook descarregou")
                self.__bateria.descarregar(tempo)
                self.__ligado = False
            else:
                print(f"msg: Usando por {tempo} minutos")
                self.__bateria.descarregar(tempo)
            return

        # Caso 2: apenas carregador
        if self.__carregador and not self.__bateria:
            print("msg: Notebook utilizado com sucesso")
            return

        # Caso 3: bateria + carregador
        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.get_potencia() * tempo)
            print("msg: Notebook utilizado com sucesso")
            return

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        bat_str = "Nenhuma"
        car_str = "Desconectado"

        if self.__bateria is not None:
            bat_str = f"({self.__bateria.get_carga()}/{self.__bateria.get_capacidade()})"
        if self.__carregador is not None:
            car_str = f"(Potência {self.__carregador.get_potencia()})"

        print(f"msg: Status: {status}, Bateria: {bat_str}, Carregador: {car_str}")