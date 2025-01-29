# Lista para almacenar libros
lista = []

# Mostrar el menú de la biblioteca
def mostrar_menu():
    print("Biblioteca de llibres") # Título del menú
    print("1. Afegir llibres") # Opción para añadir libros
    print("2. Cercar el llibre pel seu títol") # Opción para buscar libros por título
    print("3. Eliminar llibre pel seu títol") # Opción para eliminar libros por título
    print("4. Llistar tots els llibres de la biblioteca") # Opción para listar todos los libros
    print("5. Sortir") # Opción para salir del programa
    return input("Selecciona una opció del 1 al 5: ") # Solicita al usuario que seleccione una opción

# Añadir libros a la lista
def afegir_llibres():
    # Solicita información del libro al usuario
    titol = input("Afegeix el títol del llibre: ")
    autor = input("Afegeix l'autor del llibre: ")
    any = input("Afegeix l'any de publicació del llibre: ")

    # Crea un diccionario con la información del libro
    llibre = {
        "titol": titol,
        "autor": autor,
        "any": any,
    }

    # Añade el diccionario a la lista de libros
    lista.append(llibre)
    print(f"S'ha afegit el llibre {titol}, de l'autor {autor}, de l'any {any}.")

# Buscar libro por título
def cercar_llibre():
    # Solicita el título del libro al usuario
    titol = input("Introdueix el nom del llibre que vols cercar: ")
    
    found = False # Bandera para verificar si el libro se encuentra en la lista

    # Recorre la lista de libros
    for llibre in lista:
        if llibre["titol"] == titol: # Si encuentra un libro con el título indicado
            print(f"{titol} (De {llibre['autor']}, publicat a l'any {llibre['any']}).")
            found = True # Marca la bandera como encontrada
            break # Sale del bucle una vez que encuentra el libro
    # Si no encontró el libro, imprime un mensaje
    if not found:
        print("Aquest llibre no es troba en la biblioteca.")

# Eliminar libro por título
def eliminar_llibre():
    # Solicita el título del libro al usuario
    titol = input("Introdueix el títol del llibre que vols eliminar: ")
    found = False # Bandera para verificar si el libro se encuentra en la lista

    # Recorre la lista de libros
    for llibre in lista:
        if llibre["titol"] == titol: # Si encuentra un libro con el título indicado
            lista.remove(llibre) # Elimina el libro de la lista
            print(f"El llibre amb títol: {titol} a estat eliminat.")
            found = True # Marca la bandera como encontrada
            break # Sale del bucle una vez que elimina el libro

    # Si no encontró el libro para eliminar, imprime un mensaje
    if not found:
        print("Aquest llibre no es pot eliminar perquè no existeix.")

# Listar todos los libros
def llistar_llibres():
    if lista: # Si hay libros en la lista
        print("Llibres en la biblioteca: ")
        # Recorre la lista de libros e imprime cada uno
        for llibre in lista:
            print(f"{llibre['titol']} (De {llibre['autor']}, publicat a l'any {llibre['any']}).")
    else: # Si la lista está vacía, imprime un mensaje
        print("No hi ha llibres en la biblioteca!!")

# Función principal de la biblioteca de libros
def biblioteca_llibres():
    while True: # Bucle infinito para mantener el programa en ejecución hasta que el usuario salga
        opcion = mostrar_menu() # Muestra el menú y solicita una opción

        # Ejecuta la función correspondiente según la opción seleccionada por el usuario
        if opcion == "1":
            afegir_llibres()
        elif opcion == "2":
            cercar_llibre()
        elif opcion == "3":
            eliminar_llibre()
        elif opcion == "4":
            llistar_llibres()
        elif opcion == "5":
            print("Sortint del programa...")
            break # Rompe el bucle y sale del programa
        else: 
            print("Opció no vàlida, torna-ho a intentar!") # Mensaje para opciones no válidas
# Ejecuta el programa de la biblioteca de libros
biblioteca_llibres()