tareas = []

def mostrar_menu():
    print("\n--- LISTA DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        tareas.append(tarea)
        print("✔ Tarea agregada")

    elif opcion == "2":
        print("\nTareas:")
        for i, t in enumerate(tareas):
            print(f"{i + 1}. {t}")

    elif opcion == "3":
        num = int(input("Número de tarea a eliminar: "))
        if 0 < num <= len(tareas):
            tareas.pop(num - 1)
            print("✔ Tarea eliminada")
        else:
            print("Número inválido")

    elif opcion == "4":
        print("Adiós 👋")
        break

    else:
        print("Opción inválida")