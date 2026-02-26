# To-Do List para cursos de Mauricio

tareas = [
    {"curso": "Fotografía", "tarea": "Practicar iluminación", "completada": False},
    {"curso": "Marketing Digital", "tarea": "Estudiar embudo de ventas", "completada": False},
    {"curso": "Programación", "tarea": "Practicar condicionales en Python", "completada": False}
]

def mostrar_tareas():
    print("\n=== LISTA DE TAREAS ===")
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i + 1}. [{estado}] {tarea['curso']} - {tarea['tarea']}")

def marcar_completada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

def menu():
    while True:
        mostrar_tareas()
        print("\nOpciones:")
        print("1. Marcar tarea como completada")
        print("2. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = int(input("Número de la tarea: ")) - 1
            marcar_completada(numero)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()