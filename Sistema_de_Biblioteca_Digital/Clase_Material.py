from ClaseHijas import Libro, Revista, Periodico
from Clase_Material import Material


materiales = []
def agregar_material(material):
    if isinstance(material, Material):
        materiales.append(material)
        print(f" Material '{material.titulo}' agregado a la lista.")
    else:
        print(" Solo se pueden agregar objetos de tipo Material.")

def mostrar_materiales():
    if not materiales:
        print(" La lista de materiales está vacía.")
        return
    print(" Lista de Materiales:")
    for material in materiales:
        print(f" - {material.descripcion()} (Precio: ${material.get_precio()})")
# Ejemplo de uso
if __name__ == "__main__":
    libro = Libro("El Quijote", "Miguel de Cervantes", 300, 863)
    revista = Revista("1984", "George Orwell", 250, 2)
    periodico = Periodico("Cien Años de Soledad", "Gabriel García Márquez", 400, "2023-10-03")

    agregar_material(libro)
    agregar_material(revista)
    agregar_material(periodico)

    mostrar_materiales()
