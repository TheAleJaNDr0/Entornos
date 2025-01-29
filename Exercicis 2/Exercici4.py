def ejercicio():
    A = int(input("Introduce un valor cualquiera"))
    B = int(input("Introduce otro valor cualquiera"))
    C = int(input("Introduce un tercer valor cualquiera"))
    if A > B and  A > C:
        print(f"El valor mayor de los tres es {A}")
    elif B > A and B > C:
        print(f"El valor mayor de los tres es {B}")
    elif C > A and C > B:
        print(f"El valor mayor de los tres es {C}")
    else:
        print(f"Los valores son iguales {A} = {B} = {C}")

if __name__ == "__main__":
    ejercicio()   
