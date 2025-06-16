# Criando uma classe abstrata
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__ (self, nome, preco):
        self._nome = nome
        self._preco = preco


    # Obriga todas as classes que sao derivadas de ItemCardapio a implementar esse metodo
    @abstractmethod
    def aplicar_desconto (self):
        pass
    
