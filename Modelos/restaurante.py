from Modelos.avaliacao import Avaliacao

class Restaurante:
    # self é a referência ao objeto que está sendo criado 

    lista_restaurantes = []  # Atributo de classe, compartilhado por todas as instâncias

    # __init__ é o método construtor, chamado quando um objeto é criado
    def __init__(self, nome, categoria):
        # Atributo privado, indicado pelo underscore
        self._nome = nome.title()  # Converte o nome para título
        self._categoria = categoria.upper() # Converte a categoria para maiúsculas
        self._ativo = False 
        self._avaliacao = [] # Quando criamos um restaurante ele ja inicia ele com uma lista de avaliacoes
        Restaurante.lista_restaurantes.append(self)


    # __str__ é o método que define como o objeto será representado como string
    def __str__(self):
        return f"{self._nome} | {self._categoria}"


    # lista_restaurantes é um método de classe que lista todos os restaurantes
    @classmethod # Decorador de classe, permite acessar o método sem instanciar a classe
    def listar_restaurantes(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)}| {"Status"}")
        for restaurante in cls.lista_restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")


    # Property é um decorador que permite acessar métodos como se fossem atributos
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"


    # Alterna o status do restaurante entre ativo e inativo
    def alternar_status(self):
        self._ativo = not self._ativo


    # Recebe as avaliacoes dos restaurantes
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota) # Instanciamento do objeto Avaliacao (cliente, nota)
        self._avaliacao.append(avaliacao) # Inseri o objeto na lista


    @property
    def media_avaliacoes(self):
        if not self._avaliacao: # caso nao tenha nenhuma avaliacao do restaurante retorna o valor 0
            return 0
        
        # Soma todas as notas da lista self._avaliacao com o metodo sum
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qntd_de_notas = len(self._avaliacao) # Recebe a quantidade de objetos/notas inseridas na lista
        media = round(soma_das_notas / qntd_de_notas, 1) # Realiza a conta da media com o metodo round para deixar apenas com uma casa decimal
        return media

# TESTES 

# Instantiação de objetos da classe Restaurante

# restaurante_cocobambu = Restaurante("Coco Bambu", "Frutos do Mar")
# restaurante_cocobambu.alternar_status()  # Alterna o status do restaurante para ativo
# restaurante_outback = Restaurante("Outback", "Carnes")

# Lista de restaurantes

# Restaurante.listar_restaurantes() # Restaurante.lista_restaurantes é um método de classe, então é chamado diretamente na classe

# Dir printa os métodos e atributos do objeto 
# print(dir(restaurante_cocobambu)) 
# Vars printa o dicionário de atributos do objeto
# print(vars(restaurante_cocobambu))