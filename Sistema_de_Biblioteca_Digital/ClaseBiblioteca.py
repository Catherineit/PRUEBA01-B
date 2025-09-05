##Clase Biblioteca
# ===========================================
from ClaseHijas import Libro, Revista, Periodico

class Biblioteca:
    def __init__(self):
        self.catalogo = []  # Lista para almacenar materiales

    def agregar_material(self, material):
        if isinstance(material, (Libro, Revista, Periodico)):
            self.catalogo.append(material)
            print(f" Material '{material.titulo}' agregado al catálogo.")
        else:
            print(" Solo se pueden agregar libros, revistas o periódicos.")

    def mostrar_catalogo(self):
        if not self.catalogo:
            print(" El catálogo está vacío.")
            return
        print(" Catálogo de la Biblioteca:")
        for material in self.catalogo:
            print(f" - {material.descripcion()} (Precio: ${material.get_precio()})")
