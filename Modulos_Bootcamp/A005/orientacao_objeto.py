import datetime
import math


class Pessoa:

    def __init__(self, nome: str, sobrenome: str, data_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome} tem {self.idade} anos'



    
mateus = Pessoa(nome='Mateus', sobrenome='Moura', data_nascimento=datetime.date(1997,11, 4))
print(mateus)




