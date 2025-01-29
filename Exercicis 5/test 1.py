# Importamos las funciones necesarias de biblioteca.py
from biblioteca import afegir_llibres, cercar_llibre, eliminar_llibre, llistar_llibres, lista

# Test para añadir libros a la biblioteca
def test_afegir_llibres():
    print("Test afegir_llibres") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de añadir un nuevo libro
    afegir_llibres() # Llama a la función para añadir un libro
    assert lista, "El llibre no s'ha afegit correctament" # Verifica que el libro ha sido añadido
    print("Test afegir_llibres passed.") # Confirmación de que el test ha pasado

# Test para buscar un libro existente
def test_cercar_llibre_existent():
    print("Test cercar_llibre_existent") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de añadir un nuevo libro
    lista.append({
        "titol": "El Quijote", # Añadimos un libro de ejemplo
        "autor": "Miguel de Cervantes",
        "any": "1605"
    })
    cercar_llibre() # Llama a la función para buscar el libro
    print("Test cercar_llibre_existent passed.") # Confirmación de que el test ha pasado

# Test para buscar un libro no existente
def test_cercar_llibre_no_existent():
    print("Test cercar_llibre_no_existent") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de buscar el libro
    cercar_llibre() # Llama a la función para buscar el libro
    print("Test cercar_llibre_no_existent passed.") # Confirmación de que el test ha pasado

# Test para eliminar un libro existente
def test_eliminar_llibre_existent():
    print("Test eliminar_llibre_existent") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de añadir un nuevo libro
    lista.append({
        "titol": "El Quijote", # Añadimos un libro de ejemplo
        "autor": "Miguel de Cervantes",
        "any": "1605"
    })
    eliminar_llibre() # Llama a la función para eliminar el libro
    assert not lista, "El llibre no s'ha eliminat correctament" # Verifica que el libro ha sido eliminado
    print("Test eliminar_llibre_existent passed.") # Confirmación de que el test ha pasado

# Test para eliminar un libro no existente
def test_eliminar_llibre_no_existent():
    print("Test eliminar_llibre_no_existent") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de intentar eliminar un libro
    eliminar_llibre() # Llama a la función para eliminar el libro
    print("Test eliminar_llibre_no_existent passed.") # Confirmación de que el test ha pasado

# Test para listar todos los libros en la biblioteca
def test_llistar_llibres():
    print("Test llistar_llibres") # Información sobre el test que se ejecuta
    lista.clear() # Limpiar la lista antes de añadir un nuevo libro
    afegir_llibres() # Añadir un libro
    llistar_llibres() # Llama a la función para listar todos los libros
    assert lista, "No es llisten els llibres correctament" # Verifica que los libros son listados correctamente
    print("Test llistar_llibres passed.") # Confirmación de que el test ha pasado

# Ejecutamos todas las pruebas
if __name__ == "__main__":
    test_afegir_llibres()
    test_cercar_llibre_existent()
    test_cercar_llibre_no_existent()
    test_eliminar_llibre_existent()
    test_eliminar_llibre_no_existent()
    test_llistar_llibres()