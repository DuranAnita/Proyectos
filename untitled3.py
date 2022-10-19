class Basquetbol:
    def __init__(self, edad, nombre, altura, peso, categoria):
        self.edad = edad
        self.nombre = nombre
        self.altura = altura
        self.peso= peso
        self.categoria = categoria
l1 = Basquetbol(18,'Ana', 1.65, 57, 'femenina')

print(l1.edad)
print(l1.nombre)
print(l1.altura)
print(l1.peso)
print(l1.categoria)