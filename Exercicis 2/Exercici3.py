def ejercicio():
    A = int(input("Introduce un valor cualquiera"))
    B = int(input("Introduce otro valor cualquiera"))
    if A > B:
        print(f"La división entre el valor mayor y el valor menor es {A/B}")
    elif A < B:
            print(f"La división entre el valor mayor y el valor menor es {B/A}")
    else:
        print(f"Los valores son iguales {A} = {B}")

if __name__ == "__main__":
    ejercicio()
