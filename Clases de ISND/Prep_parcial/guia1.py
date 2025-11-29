clientes_info = []
servicios = {
    "WD": "Desarrollo Web",
    "DS": "Ciencia de Datos",
    "ML": "Machine Learning aplicado",
    "API": "Desarrollo de APIs Empresariales"
}
servicios_contratados = []

def registrar_cliente(clientes_info):
    print("\n--- REGISTRAR CLIENTE ---")

    dui = input("Ingrese su DUI (formato 00000000-0): ")

    # Validación simple: largo exacto
    if len(dui) != 10:
        print("DUI inválido.")
        return

    # Validar que no esté repetido
    for cliente in clientes_info:
        if cliente["DUI"] == dui:
            print("Este DUI ya está registrado.")
            return

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    # Validaciones básicas
    if len(nombre) < 2 or len(apellido) < 2:
        print("El nombre o apellido es demasiado corto.")
        return

    cliente = {
        "DUI": dui,
        "Nombre": nombre,
        "Apellido": apellido
    }

    clientes_info.append(cliente)
    print("Cliente registrado exitosamente.")
    
def buscar_cliente(clientes_info, dui):
    for cliente in clientes_info:
        if cliente["DUI"] == dui:
            return True
    return False


def ya_tiene_servicio(servicios_contratados, dui):
    for contrato in servicios_contratados:
        if contrato["DUI"] == dui:
            return True
    return False

def contratar_servicio(clientes_info, servicios, servicios_contratados):
    print("\n--- CONTRATAR SERVICIO ---")

    dui = input("Ingrese el DUI del cliente: ")

    # 1. Verificar que exista
    if not buscar_cliente(clientes_info, dui):
        print("Este cliente no está registrado.")
        return

    # 2. Verificar si ya tiene servicio
    if ya_tiene_servicio(servicios_contratados, dui):
        print("Este cliente ya tiene un servicio contratado.")
        return

    # 3. Mostrar servicios
    print("\nServicios disponibles:")
    for codigo, nombre in servicios.items():
        print(f"{codigo}: {nombre}")

    servicio = input("Ingrese el código del servicio: ").upper()

    # Validar que el servicio exista
    if servicio not in servicios:
        print("Código de servicio inválido.")
        return

    contrato = {"DUI": dui, "Servicio": servicio}
    servicios_contratados.append(contrato)

    print("Servicio contratado exitosamente.")

def mostrar_contrataciones(servicios_contratados, servicios):
    print("\n--- LISTA DE CONTRATACIONES ---")

    print("Seleccione un servicio:")
    print("1. WD")
    print("2. DS")
    print("3. ML")
    print("4. API")

    opcion = input("Ingrese opción: ")

    opciones = {"1": "WD", "2": "DS", "3": "ML", "4": "API"}

    if opcion not in opciones:
        print("Opción inválida.")
        return

    codigo = opciones[opcion]
    hay = False

    print(f"\nClientes que contrataron {servicios[codigo]}:")

    for contrato in servicios_contratados:
        if contrato["Servicio"] == codigo:
            print(f"- DUI: {contrato['DUI']}")
            hay = True

    if not hay:
        print("Nadie ha contratado este servicio.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar cliente")
        print("2. Contratar servicio")
        print("3. Mostrar contrataciones por tipo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente(clientes_info)
        elif opcion == "2":
            contratar_servicio(clientes_info, servicios, servicios_contratados)
        elif opcion == "3":
            mostrar_contrataciones(servicios_contratados, servicios)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")
