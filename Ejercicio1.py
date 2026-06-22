def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def leer_menu():

    mostrar_menu()

    opcion = input("Selecciona una opcion\n")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
        print("Opcion no valida")
        mostrar_menu()
        opcion = input("Selecciona una opcion\n")
    return opcion

def agregar_estudiante(lista):
    
    print("\n---Registrar nuevo estudiante---")

    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        nota = float(input("Ingrese la nota del estudiante: "))

        if nombre.strip() == " ":
            print("Error, no puede estar vacio el nombre")
        
        elif edad <= 0:
            print("Error, debe ser un numeor entero mayor a 0")
        
        elif nota < 1.0 and nota > 7.0:
            print("Error, la nota debe ser un numero decimal entre 1.0 y 7.0") 
        
        else:
            estudiante = {
                "nombre":nombre,
                "edad":edad,
                "nota":nota,
                "aprobado":False
            }
            lista.append(estudiante)
            print("Estudiante agregado")
    except ValueError:
        print("Error, solo numeros enteros")

def Buscar_estudiante(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            return i
    return -1

lista_estudiante = []

while True:
    opcion = leer_menu()
    if opcion == "1":
        agregar_estudiante(lista_estudiante)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante\n")
        posicion = Buscar_estudiante(lista_estudiante,nombre)
        if posicion == -1:
            print("Estudiante no encontrado")
        
        else:
            print("Estudiante encontrado")
            print(f"nombre:{lista_estudiante[posicion]['nombre']}")
            print(f"Edad:{lista_estudiante[posicion]['edad']}")
            print(f"nota:{lista_estudiante[posicion]['nota']}")
    
    elif opcion == "3":
        eliminar = input("¿Que estudiante desea eliminar?\n")
        posicion = Buscar_estudiante(lista_estudiante,eliminar)

        if opcion == -1:
            print(f"Error, El estudiante {nombre} no se encuentra registrado")
        
        elif posicion == True:
            del (lista_estudiante, nombre)

    elif opcion == "4":
        if lista_estudiante[posicion]['nota'] > 4.0:
            ["aprobado"]
        else:
            ["reprobado"]
        nuevo_estado = "aprobado" if lista_estudiante[posicion]['nota']["aprobado"] else "reprobado"
        print(f"Estudiante actualizado con exito a: {nuevo_estado}")

    elif opcion == "5":
        if len(lista_estudiante) == 0:
            print("No hay estaudiante registrado")
        
        else:
            for e in lista_estudiante:
                estado = "aprobado" if e["aprobado"] else "reprobado"
                print(f"nombre: {e['nombre']} | edad: {e['edad']} | nota: {e['nota']} | estado: {estado}")
                print("-" *40)
    
    elif opcion == "6":
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    