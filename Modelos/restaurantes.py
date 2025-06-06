class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_cocobambu = Restaurante()
restaurante_cocobambu.nome = "Coco Bambu"
restaurante_cocobambu.categoria = "Frutos do Mar"

# Dir printa os métodos e atributos do objeto 
print(dir(restaurante_cocobambu)) 
# Vars printa o dicionário de atributos do objeto
print(vars(restaurante_cocobambu))

