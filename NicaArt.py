import datetime
import re

# ==========================================
# MODELOS / CLASES
# ==========================================

class Artista:
    def __init__(self, id_artista: int, nombre: str, nacionalidad: str, estilo: str):
        self.id_artista = id_artista
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.estilo = estilo

    def __str__(self):
        return f"ID: {self.id_artista} | Nombre: {self.nombre} | Nacionalidad: {self.nacionalidad} | Estilo: {self.estilo}"


class Comprador:
    def __init__(self, id_comprador: int, nombre: str, correo: str, telefono: str):
        self.id_comprador = id_comprador
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id_comprador} | Nombre: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}"


class Galeria:
    def __init__(self, id_galeria: int, nombre: str, direccion: str, encargado: str):
        self.id_galeria = id_galeria
        self.nombre = nombre
        self.direccion = direccion
        self.encargado = encargado

    def __str__(self):
        return f"ID: {self.id_galeria} | Nombre: {self.nombre} | Dirección: {self.direccion} | Encargado: {self.encargado}"


class Obra:
    def __init__(self, id_obra: int, titulo: str, precio: float, id_artista: int, id_galeria: int, disponible: bool = True):
        self.id_obra = id_obra
        self.titulo = titulo
        self.precio = precio
        self.id_artista = id_artista
        self.id_galeria = id_galeria
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Vendida"
        return f"ID: {self.id_obra} | Título: {self.titulo} | Precio: ${self.precio:,.2f} | ID Artista: {self.id_artista} | ID Galería: {self.id_galeria} | Estado: {estado}"


class Transaccion:
    def __init__(self, id_transaccion: int, id_obra: int, id_comprador: int, monto: float, fecha: str = None):
        self.id_transaccion = id_transaccion
        self.id_obra = id_obra
        self.id_comprador = id_comprador
        self.monto = monto
        self.fecha = fecha if fecha else datetime.date.today().strftime("%Y-%m-%d")

    def __str__(self):
        return f"ID Venta: {self.id_transaccion} | Fecha: {self.fecha} | ID Obra: {self.id_obra} | ID Comprador: {self.id_comprador} | Monto: ${self.monto:,.2f}"


# ==========================================
# FUNCIONES AUXILIARES DE VALIDACIÓN
# ==========================================

def leer_texto_no_vacio(mensaje: str) -> str:
    """Solicita un texto y no permite entradas vacías."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  [X] Error: Este campo no puede estar vacío.")

def leer_correo(mensaje: str) -> str:
    """Valida formato básico de correo electrónico."""
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        correo = input(mensaje).strip()
        if re.match(patron, correo):
            return correo
        print("  [X] Error: Ingrese un correo electrónico válido (ejemplo: usuario@dominio.com).")

def leer_telefono(mensaje: str) -> str:
    """Valida formato de número telefónico (dígitos y opcionalmente guiones/espacios)."""
    patron = r'^[0-9\s\-]{8,15}$'
    while True:
        telefono = input(mensaje).strip()
        if re.match(patron, telefono):
            return telefono
        print("  [X] Error: Ingrese un número de teléfono válido (mínimo 8 dígitos).")

def leer_float_positivo(mensaje: str) -> float:
    """Solicita un número flotante strictly mayor que 0."""
    while True:
        try:
            val_str = input(mensaje).strip()
            valor = float(val_str)
            if valor > 0:
                return valor
            print("  [X] Error: El valor debe ser mayor a 0.")
        except ValueError:
            print("  [X] Error: Ingrese un número válido (ejemplo: 1200.50).")

def leer_entero_positivo(mensaje: str) -> int:
    """Solicita un número entero positivo."""
    while True:
        try:
            val_str = input(mensaje).strip()
            valor = int(val_str)
            if valor > 0:
                return valor
            print("  [X] Error: El ID debe ser un número entero mayor a 0.")
        except ValueError:
            print("  [X] Error: Entrada inválida. Debe ingresar un número entero.")


# ==========================================
# SISTEMA DE GESTIÓN CON VALIDACIONES EN MEMORIA
# ==========================================

class SistemaComercioArtes:
    def __init__(self):
        self.artistas = []
        self.compradores = []
        self.galerias = []
        self.obras = []
        self.transacciones = []

        self._sec_artista = 1
        self._sec_comprador = 1
        self._sec_galeria = 1
        self._sec_obra = 1
        self._sec_transaccion = 1

        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        """Carga de datos de prueba válidos."""
        self.agregar_artista("Armando Morales", "Nicaragüense", "Óleo / Expresionismo")
        self.agregar_comprador("Carlos Mendoza", "carlos@gmail.com", "8888-8888")
        self.agregar_galeria("Galería Códice", "Managua, Nicaragua", "Ana María")
        self.agregar_obra("Selva Tropical", 4500.00, 1, 1)

    # ------------------ MÉTODOS DE BÚSQUEDA ------------------
    def buscar_artista_por_id(self, id_artista: int):
        return next((a for a in self.artistas if a.id_artista == id_artista), None)

    def buscar_comprador_por_id(self, id_comprador: int):
        return next((c for c in self.compradores if c.id_comprador == id_comprador), None)

    def buscar_galeria_por_id(self, id_galeria: int):
        return next((g for g in self.galerias if g.id_galeria == id_galeria), None)

    def buscar_obra_por_id(self, id_obra: int):
        return next((o for o in self.obras if o.id_obra == id_obra), None)

    # ------------------ ARTISTAS ------------------
    def agregar_artista(self, nombre: str, nacionalidad: str, estilo: str):
        artista = Artista(self._sec_artista, nombre, nacionalidad, estilo)
        self.artistas.append(artista)
        self._sec_artista += 1
        return artista

    def listar_artistas(self):
        if not self.artistas:
            print("\n  [!] No hay artistas registrados.")
            return False
        print("\n--- LISTA DE ARTISTAS ---")
        for a in self.artistas:
            print(f"  {a}")
        return True

    # ------------------ COMPRADORES ------------------
    def agregar_comprador(self, nombre: str, correo: str, telefono: str):
        comprador = Comprador(self._sec_comprador, nombre, correo, telefono)
        self.compradores.append(comprador)
        self._sec_comprador += 1
        return comprador

    def listar_compradores(self):
        if not self.compradores:
            print("\n  [!] No hay compradores registrados.")
            return False
        print("\n--- LISTA DE COMPRADORES ---")
        for c in self.compradores:
            print(f"  {c}")
        return True

    # ------------------ GALERÍAS ------------------
    def agregar_galeria(self, nombre: str, direccion: str, encargado: str):
        galeria = Galeria(self._sec_galeria, nombre, direccion, encargado)
        self.galerias.append(galeria)
        self._sec_galeria += 1
        return galeria

    def listar_galerias(self):
        if not self.galerias:
            print("\n  [!] No hay galerías registradas.")
            return False
        print("\n--- LISTA DE GALERÍAS ---")
        for g in self.galerias:
            print(f"  {g}")
        return True

    # ------------------ OBRAS ------------------
    def agregar_obra(self, titulo: str, precio: float, id_artista: int, id_galeria: int):
        obra = Obra(self._sec_obra, titulo, precio, id_artista, id_galeria)
        self.obras.append(obra)
        self._sec_obra += 1
        return obra

    def listar_obras(self):
        if not self.obras:
            print("\n  [!] No hay obras registradas.")
            return False
        print("\n--- LISTA DE OBRAS DE ARTE ---")
        for o in self.obras:
            print(f"  {o}")
        return True

    # ------------------ TRANSACCIONES ------------------
    def registrar_transaccion(self, id_obra: int, id_comprador: int):
        obra = self.buscar_obra_por_id(id_obra)
        comprador = self.buscar_comprador_por_id(id_comprador)

        if not obra:
            print("\n  [X] Error: No existe ninguna obra con el ID ingresado.")
            return False
        if not obra.disponible:
            print("\n  [X] Error: La obra seleccionada ya fue vendida previamente.")
            return False
        if not comprador:
            print("\n  [X] Error: No existe ningún comprador con el ID ingresado.")
            return False

        obra.disponible = False
        transaccion = Transaccion(self._sec_transaccion, id_obra, id_comprador, obra.precio)
        self.transacciones.append(transaccion)
        self._sec_transaccion += 1
        print(f"\n  [✓] Venta registrada con éxito. Número de Transacción: {transaccion.id_transaccion}")
        return True

    def listar_transacciones(self):
        if not self.transacciones:
            print("\n  [!] No hay ventas/transacciones registradas.")
            return False
        print("\n--- HISTORIAL DE TRANSACCIONES ---")
        for t in self.transacciones:
            print(f"  {t}")
        return True

    # ------------------ DASHBOARD ------------------
    def mostrar_dashboard(self):
        total_obras = len(self.obras)
        obras_disponibles = len([o for o in self.obras if o.disponible])
        obras_vendidas = total_obras - obras_disponibles
        ingresos_totales = sum(t.monto for t in self.transacciones)

        print("\n==========================================")
        print("          DASHBOARD DE RESUMEN            ")
        print("==========================================")
        print(f" Total de Artistas registrados:    {len(self.artistas)}")
        print(f" Total de Compradores registrados: {len(self.compradores)}")
        print(f" Total de Galerías registradas:   {len(self.galerias)}")
        print(f" Total de Obras:                   {total_obras} (Disponibles: {obras_disponibles} | Vendidas: {obras_vendidas})")
        print(f" Total de Ventas realizadas:       {len(self.transacciones)}")
        print(f" Ingresos totales por ventas:     ${ingresos_totales:,.2f}")
        print("==========================================\n")


# ==========================================
# INTERFAZ Y FLUJO POR CONSOLA
# ==========================================

def menu_principal():
    sistema = SistemaComercioArtes()

    while True:
        print("\n" + "="*45)
        print("    SISTEMA COMERCIO ARTES - MENÚ PRINCIPAL")
        print("="*45)
        print(" 1. Dashboard (Resumen General)")
        print(" 2. Gestión de Artistas")
        print(" 3. Gestión de Compradores")
        print(" 4. Gestión de Galerías")
        print(" 5. Gestión de Obras de Arte")
        print(" 6. Registrar Transacción / Venta")
        print(" 7. Ver Historial de Transacciones")
        print(" 0. Salir del Sistema")
        print("-" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            sistema.mostrar_dashboard()

        elif opcion == "2":
            sub_menu_artistas(sistema)

        elif opcion == "3":
            sub_menu_compradores(sistema)

        elif opcion == "4":
            sub_menu_galerias(sistema)

        elif opcion == "5":
            sub_menu_obras(sistema)

        elif opcion == "6":
            registrar_venta_flujo(sistema)

        elif opcion == "7":
            sistema.listar_transacciones()

        elif opcion == "0":
            print("\nGracias por utilizar el Sistema ComercioArtes.")
            break
        else:
            print("\n  [X] Opción inválida. Ingrese un número del 0 al 7.")


def sub_menu_artistas(sistema: SistemaComercioArtes):
    while True:
        print("\n--- GESTIÓN DE ARTISTAS ---")
        print(" 1. Listar Artistas")
        print(" 2. Registrar Artista")
        print(" 0. Volver al Menú Principal")
        opc = input("Seleccione una opción: ").strip()

        if opc == "1":
            sistema.listar_artistas()
        elif opc == "2":
            print("\n--- REGISTRAR ARTISTA ---")
            nombre = leer_texto_no_vacio("Ingrese Nombre completo: ")
            nacionalidad = leer_texto_no_vacio("Ingrese Nacionalidad: ")
            estilo = leer_texto_no_vacio("Ingrese Estilo/Técnica: ")
            sistema.agregar_artista(nombre, nacionalidad, estilo)
            print("  [✓] Artista registrado correctamente.")
        elif opc == "0":
            break
        else:
            print("  [X] Opción inválida.")


def sub_menu_compradores(sistema: SistemaComercioArtes):
    while True:
        print("\n--- GESTIÓN DE COMPRADORES ---")
        print(" 1. Listar Compradores")
        print(" 2. Registrar Comprador")
        print(" 0. Volver al Menú Principal")
        opc = input("Seleccione una opción: ").strip()

        if opc == "1":
            sistema.listar_compradores()
        elif opc == "2":
            print("\n--- REGISTRAR COMPRADOR ---")
            nombre = leer_texto_no_vacio("Ingrese Nombre completo: ")
            correo = leer_correo("Ingrese Correo electrónico: ")
            telefono = leer_telefono("Ingrese Teléfono: ")
            sistema.agregar_comprador(nombre, correo, telefono)
            print("  [✓] Comprador registrado correctamente.")
        elif opc == "0":
            break
        else:
            print("  [X] Opción inválida.")


def sub_menu_galerias(sistema: SistemaComercioArtes):
    while True:
        print("\n--- GESTIÓN DE GALERÍAS ---")
        print(" 1. Listar Galerías")
        print(" 2. Registrar Galería")
        print(" 0. Volver al Menú Principal")
        opc = input("Seleccione una opción: ").strip()

        if opc == "1":
            sistema.listar_galerias()
        elif opc == "2":
            print("\n--- REGISTRAR GALERÍA ---")
            nombre = leer_texto_no_vacio("Ingrese Nombre de la Galería: ")
            direccion = leer_texto_no_vacio("Ingrese Dirección: ")
            encargado = leer_texto_no_vacio("Ingrese Nombre del Encargado: ")
            sistema.agregar_galeria(nombre, direccion, encargado)
            print("  [✓] Galería registrada correctamente.")
        elif opc == "0":
            break
        else:
            print("  [X] Opción inválida.")


def sub_menu_obras(sistema: SistemaComercioArtes):
    while True:
        print("\n--- GESTIÓN DE OBRAS DE ARTE ---")
        print(" 1. Listar Obras")
        print(" 2. Registrar Nueva Obra")
        print(" 0. Volver al Menú Principal")
        opc = input("Seleccione una opción: ").strip()

        if opc == "1":
            sistema.listar_obras()
        elif opc == "2":
            if not sistema.artistas:
                print("  [X] No se pueden agregar obras. Debe haber al menos un Artista registrado.")
                continue
            if not sistema.galerias:
                print("  [X] No se pueden agregar obras. Debe haber al menos una Galería registrada.")
                continue

            print("\n--- REGISTRAR OBRA DE ARTE ---")
            titulo = leer_texto_no_vacio("Título de la obra: ")
            precio = leer_float_positivo("Precio ($): ")

            sistema.listar_artistas()
            while True:
                id_art = leer_entero_positivo("Ingrese el ID del Artista asignado: ")
                if sistema.buscar_artista_por_id(id_art):
                    break
                print("  [X] Error: El ID del Artista no existe en el sistema.")

            sistema.listar_galerias()
            while True:
                id_gal = leer_entero_positivo("Ingrese el ID de la Galería asignada: ")
                if sistema.buscar_galeria_por_id(id_gal):
                    break
                print("  [X] Error: El ID de la Galería no existe en el sistema.")

            sistema.agregar_obra(titulo, precio, id_art, id_gal)
            print("  [✓] Obra registrada correctamente.")

        elif opc == "0":
            break
        else:
            print("  [X] Opción inválida.")


def registrar_venta_flujo(sistema: SistemaComercioArtes):
    print("\n--- REGISTRAR TRANSACCIÓN / VENTA ---")
    
    # Validar que existan obras disponibles y compradores registrados
    obras_disponibles = [o for o in sistema.obras if o.disponible]
    if not obras_disponibles:
        print("  [!] No hay obras disponibles para venta.")
        return

    if not sistema.compradores:
        print("  [!] No hay compradores registrados en el sistema.")
        return

    print("\nObras disponibles:")
    for o in obras_disponibles:
        print(f"  {o}")

    while True:
        id_obra = leer_entero_positivo("\nIngrese el ID de la Obra a vender: ")
        obra = sistema.buscar_obra_por_id(id_obra)
        if obra and obra.disponible:
            break
        print("  [X] Error: Ingrese un ID de obra que exista y esté DISPONIBLE.")

    sistema.listar_compradores()
    while True:
        id_comprador = leer_entero_positivo("\nIngrese el ID del Comprador: ")
        if sistema.buscar_comprador_por_id(id_comprador):
            break
        print("  [X] Error: Ingrese un ID de comprador existente.")

    sistema.registrar_transaccion(id_obra, id_comprador)


if __name__ == "__main__":
    menu_principal()