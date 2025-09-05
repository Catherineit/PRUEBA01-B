## Programa principal (main)
# ===========================================

titulos = ["El Quijote", "1984", "Cien Años de Soledad"]
autores = ["Miguel de Cervantes", "George Orwell", "Gabriel García Márquez"]
precios = [300, 250, 400]
paginas = [863, 328, 417]
ediciones = [1, 2, 3]
fechas = ["2023-10-01", "2023-10-02", "2023-10-03"]
from ClaseBiblioteca import Biblioteca
from ClaseHijas import Libro, Revista, Periodico
from Clase_Material import Material
if __name__ == "__main__":
    # Crear instancia de Biblioteca
    biblioteca = Biblioteca()

    # Crear materiales y agregarlos a la biblioteca
    libro1 = Libro(titulos[0], autores[0], precios[0], paginas[0])
    revista1 = Revista(titulos[1], autores[1], precios[1], ediciones[1])
    periodico1 = Periodico(titulos[2], autores[2], precios[2], fechas[2])

    biblioteca.agregar_material(libro1)
    biblioteca.agregar_material(revista1)
    biblioteca.agregar_material(periodico1)

    # Mostrar catálogo completo
    biblioteca.mostrar_catalogo()


