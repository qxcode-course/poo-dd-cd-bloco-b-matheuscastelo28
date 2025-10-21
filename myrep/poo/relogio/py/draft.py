class Relogio:
    def __init__(self, hora: int, minuto: int, segundo: int):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, hora: int):
        if 0 <= hora <= 23:
            self.hora = hora
        else:
            print("fail: Hora inválida! Deve estar entre 0 e 23")

    def set_minuto(self, minuto: int):
        if 0 <= minuto <= 59:
            self.minuto = minuto
        else:
            print("fail: Minuto inválido! Deve estar entre 0 e 59")

    def set_segundo(self, segundo: int):
        if 0 <= segundo <= 59:
            self.segundo = segundo
        else:
            print("fail: Segundo inválido! Deve estar entre 0 e 59")

    def get_hora(self):
        return self.hora

    def get_minuto(self):
        return self.minuto

    def get_segundo(self):
        return self.segundo

    def toString(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def __str__(self):
        return self.toString()

    def nextSecond(self):
        self.segundo += 1
        if self.segundo > 59:
            self.segundo = 0
            self.minuto += 1
