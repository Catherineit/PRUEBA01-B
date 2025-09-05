from Clase_Material import Material
# Clases hijas que heredan de Material


class Libro(Material):
    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas

    # Sobrescribir método descripcion
    def descripcion(self):
        return f"Libro: Título {self.titulo}, Autor {self.autor}, Páginas {self.paginas}"
    
class Revista(Material):
    def __init__(self, titulo, autor, precio, edicion):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion

    # Sobrescribir método descripcion
    def descripcion(self):
        return f"Revista: Título {self.titulo}, Autor {self.autor}, Edición {self.edicion}"
    
class Periodico(Material):
    def __init__(self, titulo, autor, precio, fecha):
        super().__init__(titulo, autor, precio)
        self.fecha = fecha

    # Sobrescribir método descripcion
    def descripcion(self):
        return f"Periódico: Título {self.titulo}, Autor {self.autor}, Fecha {self.fecha}"

