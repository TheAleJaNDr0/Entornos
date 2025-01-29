if __name__ == "__main__":
    print("Introduce el número de un mes (1-12)")
    Mes = int(input())
    if Mes<0 or Mes>12:
        print("Introduce un día de ese mes")
        Dia = int(input())
    diasdelMes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if Dia > diasdelMes[Mes-1] and Dia < 0 :
        print("El día introducido no existe en el mes introducido")
