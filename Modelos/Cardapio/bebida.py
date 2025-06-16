from Modelos.Cardapio.item_cardapio import ItemCardapio

# Heranca
class Bebida (ItemCardapio):
    def __init__ (self, nome, preco, tamanho):
        # Metodo especial super para acessar os atributos da classe pai
        super().__init__(nome, preco)
        self._tamanho = tamanho
    

    def __str__ (self):
        return f"{self._nome}"