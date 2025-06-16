from Modelos.Cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__ (self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    

    def __str__ (self):
        return self._nome
    

    def aplicar_desconto(self):
        pass