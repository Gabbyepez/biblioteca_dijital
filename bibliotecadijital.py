# ==============================
# CLASE LIBRO
# ==============================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar título y autor (datos inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# ==============================
# CLASE USUARIO
# ==============================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # Lista para almacenar los libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(libro)


# ==============================
# CLASE BIBLIOTECA
# ==============================
class Biblioteca:
    def __init__(self):

        # Diccionario para almacenar libros usando ISBN como clave
        self.libros = {}

        # Diccionario para almacenar usuarios
        self.usuarios = {}

        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

    # -------------------------
    # AÑADIR LIBRO
    # -------------------------
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente.")

    # -------------------------
    # QUITAR LIBRO
    # -------------------------
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # -------------------------
    # REGISTRAR USUARIO
    # -------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")

    # -------------------------
    # ELIMINAR USUARIO
    # -------------------------
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # -------------------------
    # PRESTAR LIBRO
    # -------------------------
    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no existe.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        libro = self.libros[isbn]

        if libro.disponible:
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            libro.disponible = False
            print("Libro prestado correctamente.")
        else:
            print("El libro no está disponible.")

    # -------------------------
    # DEVOLVER LIBRO
    # -------------------------
    def devolver_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            usuario.devolver_libro(libro)
            libro.disponible = True
            print("Libro devuelto correctamente.")
        else:
            print("Datos incorrectos.")

    # -------------------------
    # BUSCAR LIBROS
    # -------------------------
    def buscar_libro(self, criterio, valor):

        resultados = []

        for libro in self.libros.values():

            if criterio == "titulo" and libro.info[0] == valor:
                resultados.append(libro)

            elif criterio == "autor" and libro.info[1] == valor:
                resultados.append(libro)

            elif criterio == "categoria" and libro.categoria == valor:
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")


# ==============================
# PRUEBAS DEL SISTEMA
# ==============================

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", "111")
libro2 = Libro("El principito", "Antoine de Saint-Exupery", "Fábula", "222")
libro3 = Libro("Python básico", "Juan Perez", "Programación", "333")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Gabriela", 1)
usuario2 = Usuario("Carlos", 2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", 1)

# Ver libros prestados
usuario1.listar_libros()

# Devolver libro
biblioteca.devolver_libro("111", 1)

# Buscar libro por autor
biblioteca.buscar_libro("autor", "Gabriel Garcia Marquez")