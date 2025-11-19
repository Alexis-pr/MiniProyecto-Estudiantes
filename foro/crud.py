import json
import os
import csv

# Lista de estudiantes
estudiantes = []

# --- Crear --- 
def crear():
    while True:
        try:
            # Ingreso del nombre
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre.isalpha():
                break
            else:
                print("El nombre debe contener solo letras.")
        except Exception as e:
            print(f"Error: {e}, intente de nuevo.")

    while True:
        try:
            # Ingreso del grado
            grado = input("Ingrese el grado del estudiante: ")
            if grado.isdigit():
                grado = int(grado)
                break
            else:
                print("El grado debe ser un número entero.")
        except Exception as e:
            print(f"Error: {e}, intente de nuevo.")

    while True:
        try:
            # Ingreso de la nota final
            notaFinal = float(input("Ingrese la nota final: "))
            if notaFinal <= 0:
                print("La nota debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("La nota final debe ser un número decimal.")

    # Guardar los datos ingresados
    guardar(nombre, grado, notaFinal)

# --- Guardar ---
def guardar(nombre, grado, notaFinal):
    datos = {
        "nombre": nombre,
        "grado": grado,
        "notaFinal": notaFinal
    }
    estudiantes.append(datos)
    print(f"Estudiante {nombre} guardado correctamente.")

# --- Mostrar ---
def mostrar():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for i, student in enumerate(estudiantes, start=1):
            print(f"Estudiante #{i}")
            print(f"Nombre: {student['nombre']}")
            print(f"Grado: {student['grado']}")
            print(f"Nota final: {student['notaFinal']}\n")

# --- Actualizar ---
def actualizar():
    try:
        actualizar_nombre = input("Ingrese el nombre del estudiante a actualizar: ")
        for student in estudiantes:
            if student["nombre"].lower() == actualizar_nombre.lower():
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                student["nombre"] = nuevo_nombre
                print("Estudiante actualizado correctamente.")
                break
        else:
            print("Estudiante no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

# --- Eliminar ---
def eliminar():
    try:
        eliminar_nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        for i, student in enumerate(estudiantes):
            if student["nombre"].lower() == eliminar_nombre.lower():
                del estudiantes[i]
                print("Estudiante eliminado correctamente.")
                break
        else:
            print("Estudiante no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

# --- Guardar en archivo JSON ---
def guardar_en_archivo():
    try:
        with open("estudiantes.json", "w", encoding="utf-8") as json_file:
            json.dump(estudiantes, json_file, ensure_ascii=False, indent=4)
        print("Datos guardados en estudiantes.json")
    except Exception as e:
        print(f"Error al guardar en archivo JSON: {e}")

# --- Convertir de JSON a CSV ---
def convertircsv():
    try:
        # Verificar si el archivo JSON existe
        if not os.path.exists('estudiantes.json'):
            print("El archivo 'estudiantes.json' no existe.")
            return

        # Leer el archivo JSON
        with open('estudiantes.json', 'r', encoding='utf-8') as datos_json:
            datos = json.load(datos_json)

            # Verificar si el archivo JSON tiene datos
            if not datos:
                print("No hay datos en el archivo JSON.")
                return

            # Obtener las claves del primer diccionario como las columnas del CSV
            dato = datos[0].keys()

            # Guardar los datos en el archivo CSV
            with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
                writer = csv.DictWriter(archivo_csv, fieldnames=dato)
                writer.writeheader()
                for i in datos:
                    writer.writerow(i)

            print("Datos convertidos y guardados en datos.csv")

    except Exception as e:
        print(f"Error al convertir JSON a CSV: {e}")

# --- Crear un directorio ---
def creardirectorio():
    try:
        nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta)
            print(f"Carpeta '{nombre_carpeta}' creada correctamente.")
        else:
            print(f"La carpeta '{nombre_carpeta}' ya existe.")
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")

# --- Menú principal ---
while True:
    print("\n1. Crear estudiante")
    print("2. Mostrar estudiantes")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Guardar en archivo JSON")
    print("6. Convertir JSON a CSV")
    print("7. Crear directorio")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        guardar_en_archivo()
    elif opcion == "6":
        convertircsv()
    elif opcion == "7":
        creardirectorio()
    elif opcion == "8":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
