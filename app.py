from Modelos.restaurante import Restaurante

restaurante_cocobambu = Restaurante("coco bambu", "frutos do mar")
restaurante_cocobambu.receber_avaliacao("Joao", 4)
restaurante_cocobambu.receber_avaliacao("Julia", 2)

restaurante_outback = Restaurante("outback", "churrascaria")

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()