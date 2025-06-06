class Restaurante:
    # self é a referência ao objeto que está sendo criado 

    lista_restaurantes = []  # Atributo de classe, compartilhado por todas as instâncias

    # __init__ é o método construtor, chamado quando um objeto é criado
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.lista_restaurantes.append(self)
    
    # __str__ é o método que define como o objeto será representado como string
    def __str__(self):
        return f"{self.nome} | {self.categoria} | {'Ativo' if self.ativo else 'Inativo'}"
    
    # lista_restaurantes é um método de classe que lista todos os restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.lista_restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {'Ativo' if restaurante.ativo else 'Inativo'}")

# Instantiação de objetos da classe Restaurante
restaurante_cocobambu = Restaurante("Coco Bambu", "Frutos do Mar")
restaurante_outback = Restaurante("Outback", "Carnes")

# Lista de restaurantes
Restaurante.listar_restaurantes() # Restaurante.lista_restaurantes é um método de classe, então é chamado diretamente na classe

# Dir printa os métodos e atributos do objeto 
# print(dir(restaurante_cocobambu)) 
# Vars printa o dicionário de atributos do objeto
# print(vars(restaurante_cocobambu))

