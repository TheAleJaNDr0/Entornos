# Diccionario global que almacenará los contactos.
agenda = {}


# Función para mostrar el menú de opciones de la agenda.
def mostrar_menu():
    print("Agenda de contactos")
    # Opciones que el usuario puede seleccionar.
    print("1. Ver contactos")
    print("2. Buscar un contacto")
    print("3. Añadir un contacto")
    print("4. Actualizar un contacto")
    print("5. Eliminar un contacto")
    print("6. Salir")
    # Solicitamos al usuario que ingrese una opción.
    return input("Selecciona una opción(1-6): ")


# Función para validar que el número de teléfono introducido sea correcto.
def validar_telefono(telefono):
    # Verifica que el teléfono solo contenga dígitos y tenga un máximo de 9 dígitos.
    return telefono.isdigit() and len(telefono) <= 9


# Función para ver todos los contactos almacenados en la agenda.
def ver_contactos():
    if agenda:
        print("Contactos en la agenda:")
        # Si la agenda tiene contactos, los muestra.
        for nombre, num in agenda.items():
            print(f"{nombre}: {num}")
    else:
        print("La agenda esta vacía.")


# Función para añadir un nuevo contacto a la agenda.
def add_contact():
    # Solicita al usuario el nombre y el número de teléfono.
    nombre = input("Nombre del contacto:")
    num = input("Número de teléfono:")
    # Valida si el número de teléfono es correcto.
    if validar_telefono(num):
        # Añade el contacto al diccionario agenda.
        agenda[nombre] = num
        print(f"Contacto añadido: {nombre} - {num}")
    else:
        # Si el número no es válido, se muestra un mensaje de error.
        print("Número de teléfono no valido. Debe ser numérico y tener un máximo de 9 dígitos.")


# Función para buscar un contacto en la agenda.
def buscar_contacto():
    # Solicita el nombre del contacto a buscar.
    nombre = input("Introduce un contacto:")
    if nombre in agenda:
        # Si el contacto existe, muestra su nombre y número.
        print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
    else:
        # Si el contacto no existe, muestra un mensaje de error.
        print("El contacto no existe.")


# Función para actualizar el número de un contacto existente.
def actualizar_contacto():
    # Solicita el nombre del contacto que se desea actualizar.
    nombre = input("Introduce el contacto a actualizar: ")
    if nombre in agenda:
        # Si el contacto existe, solicita el nuevo número de teléfono.
        nuevo_numero = input(f"Introduce el nuevo numero para {nombre}")
        # Verifica que el nuevo número sea válido.
        if validar_telefono(nuevo_numero):
            # Si es válido, actualiza el número del contacto en el diccionario agenda.
            agenda[nombre] = nuevo_numero
            print(f"Contacto actualizado: {nombre} - {nuevo_numero}")
        else:
            # Si el número no es válido, muestra un mensaje de error.
            print("Este número no es válido. Debe ser numérico y tener un máximo de 9 dígitos.")
    else:
        # Si el contacto no existe, muestra un mensaje de error.
        print("El contacto no existe.")


# Función para eliminar un contacto de la agenda.
def eliminar_contacto():
    # Solicita el nombre del contacto que se desea eliminar.
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in agenda:
        # Si el contacto existe, lo elimina del diccionario agenda.
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        # Si el contacto no existe, muestra un mensaje de error.
        print("El contacto no existe.")


# Función principal que gestiona la interacción con el usuario.
def agenda_contactos():
    while True:
        # Muestra el menú y obtiene la opción seleccionada por el usuario.
        opcion = mostrar_menu()
        # Dependiendo de la opción seleccionada, llama a la función correspondiente.
        if opcion == "1":
            ver_contactos()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            add_contact()
        elif opcion == "4":
            actualizar_contacto()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            # Si el usuario selecciona "6", sale del programa.
            print("Saliendo de la agenda...")
            break
        else:
            # Si la opción seleccionada no es válida, muestra un mensaje de error.
            print("Opción no válida. Intentalo de nuevo.")


# Llama a la función principal para ejecutar el programa.
agenda_contactos()