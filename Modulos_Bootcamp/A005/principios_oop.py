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


class Curriculo:

    def __init__(self, pessoa: Pessoa, experiencias: list[str]):
        self.pessoa = pessoa
        self.experiencias = experiencias

    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)

    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1:][0]

    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já " \
               f"trabalhou em {self.quantidade_de_experiencias} empresas e atualmente trabalha " \
               f"na empresa {self.empresa_atual}"


mateus = Pessoa(nome='Mateus', sobrenome='Moura', data_nascimento=datetime.date(1997,11, 4))
print(mateus)

curriculo_mateus = Curriculo(
    pessoa=mateus, 
    experiencias=['Loft', 'UFABC', 'Keycash', 'Ambev']
)

print(curriculo_mateus.pessoa.idade)
print(curriculo_mateus)
curriculo_mateus.adiciona_experiencia('empresa_x')
print(curriculo_mateus)


class Vivente:

    def __init__(self, nome: str, data_nascimento: datetime.date):
        self.nome = nome
        self.data_nascimento = data_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_nascimento).days / 365.2425)

    def emite_ruido(self, ruido: str):
        print(f'{self.nome} fez ruído: {ruido}')


class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f'{self.nome} tem {self.idade} anos'

    def fala(self, frase):
        return self.emite_ruido(frase)


class Cachorro(Vivente):

    def __init__(self, raca: str, nome: str, data_nascimento: datetime.date):
        super().__init__(nome, data_nascimento)
        self.raca = raca

    def __str__(self) -> str:
        return f'{self.nome} é da raça {self.raca} e tem {self.idade} anos'

    def late(self):
        return self.emite_ruido('Au! Au!')


mateus2 = PessoaHeranca(nome='Mateus', data_nascimento=datetime.date(1997,11, 4))    
print(mateus2)

nina = Cachorro(nome='Nina', data_nascimento=datetime.date(2010, 4, 15), raca='Vira Lata')

nina.late()
mateus2.fala('Para de latir, Nina!')
