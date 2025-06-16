from Modelos.restaurante import Restaurante
from Modelos.Cardapio.prato import Prato
from Modelos.Cardapio.bebida import Bebida

# restaurante_cocobambu = Restaurante("coco bambu", "frutos do mar")
# restaurante_cocobambu.receber_avaliacao("Joao", 4)
# restaurante_cocobambu.receber_avaliacao("Julia", 2)

# restaurante_outback = Restaurante("outback", "churrascaria")

# Instanciando objeto prato
prato_strogonoff = Prato("Strogonoff", 40.00, "Acompanha arroz e batata frita")

# Instanciando objeto bebida
bebida_coca = Bebida("Coca-Cola", 5.00, "350ml")

def main():
    # Restaurante.listar_restaurantes()
    print(prato_strogonoff)
    print(bebida_coca)

if __name__ == "__main__":
    main()