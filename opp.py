# objeto.atributo = valor

# classe é um modelo, com uma receita de bolo
# atributos e métodos representam objetos e situações

# class Pessoa:
#     def __init__(self, nome): # self equivale ao this em java # __init__ é para iniciar a classe (Equivale o construtor em java)
#         self.nome = nome

#     def __str__(self): # Define que todos os elementos são strings *
#         return self.nome # * falando que o nome é string

# nome_pessoa = Pessoa('Michel')
# print (nome_pessoa)

##################################################################


# ? WHAT
# class AnimalEstimacao():
#     def __init__(self, nome, especie, dono):
#         self.nome = nome
#         self.especie = especie
#         self.dono = dono

#     def __srt__(self):
#         return self.nome

# dono = AnimalEstimacao('Taina')
# especie = AnimalEstimacao('Capivara de Santa Isabel')
# nome = AnimalEstimacao('Isabellyta')

# import animal_estimacao as animal_estimacao # para importar o "arquivo" que tem a classe AnimalEstimação()
# isabellyta =  animal.AnimalEstimacao('Isabellyta', 'capivara', 'Tainah')

# print (isabellyta)

##################################################################

class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def somar(self):
        return self.n1 + self.n2

    def subtrair(self):
        return self.n1 - self.n2

    def multiplicar(self):
            return self.n1 * self.n2

    def dividir(self):
            return self.n1 / self.n2

teste = Calculadora(7, 3)
print('Soma: ', teste.somar())