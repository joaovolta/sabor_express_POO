from Modelos.Cardapio.item_cardapio import ItemCardapio 

# Heranca
class Prato (ItemCardapio):
    def __init__ (self, nome, preco, descricao):
        # Metodo especial super para acessar os atributos da classe pai
        super().__init__(nome, preco)
        self._descricao = descricao

    
    def __str__ (self):
        return f"{self._nome}"
    

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)