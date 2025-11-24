import  json
import os
import csv
#se creala libreria donde se va a capturar todos los datos ingresados
estudiantes =[]
#Nombre
#Grado 
#notaFinal

# ---- Crear ----
def crear():
    #Se crea un bucle While True para que el uurio ingrese los datos solicitado de forma correcta
    while True:
        #El Try controla los posibles errores 
        try:
            nombre = input("Ingrese el nombre del estudiante: ")
            #El isalpha sirve para confirmar que los datos ingresados son un str
            if nombre.isalpha():
                #nombre = input("Ingrese el nombre del estudiante: ")
                break
        except:
            print("Coloco un digito mal, intente de nuevo....")  

    while True:        
        try:
            #ingresa un dato por teclado como string
            grado =input("ingrese el grado del estudiante: ")

            if grado.isdigit():   # valida que sean números
                grado = int(grado) # lo combierte de string a numero
                break 
            else:
                print("no se permiten caracteres especiales")
        except:
            print("Coloco un digito mal, intente de nuevo....")   

    while True:   #continua siempre que sea verdadero         
        try:     
            notaFinal = float(input("ingrese la nota final: ")) # ingresa datos decimales
            if notaFinal <= 0: # valida que no ingresen numero negativos
                print("Nota no valida: ") #muestra el error
                print("-"*20)#multiplica los guiones x 20 para no hacerlo de forma manual
                continue #continua el código para en la siguiente linea salir del try y volver a pedir el dato
            break 
        except:
            print("Error, vuelva ingresar su nota")

    # datos = {
    #     "nombre" : nombre,
    #     "grado": grado,
    #     "notaFinal" : notaFinal
    # }
    guardar(nombre,grado,notaFinal) #guarda los datos ingresados por teclado

#--- guardar ---
def guardar(nombre,grado,notaFinal): # funcion que toma 3 parametros y los guarda a la lista
    datos = {
        "nombre" : nombre,
        "grado": grado,
        "notaFinal" : notaFinal
    }
    estudiantes.append(datos) # guarda los datos a la lista estudiante


# --- mostrar ---
def mostrar():
    global estudiantes
    if not estudiantes: # valida que la lista estudiante no este vacia
        if os.path.exists("estudiantes.json"):
            print("Cargando estudiantes desde el archivo JSON...")
            with open("estudiantes.json", "r") as f:
                estudiantes = json.load(f)
            imprimirEstudiantes()
        else:
            print("no existe ningun listado de estudiantes..")
    else:
        imprimirEstudiantes()
            

def imprimirEstudiantes():
    for i, estudent in enumerate(estudiantes, start=1): # se crea dos variables para almacenar la posicion ( clave, valor)
        print(f"el estudiante #{i}")# muestra el ID o numero de la posicion
        # la F dentro del prin permite concatenar texto y variables dentro de las llaves
        #estudent[i]["grado"]

        #imprime los valores
        print(f" se llama {estudent["nombre"]}")            
        print(f"El grado es {estudent["grado"]}")
        print(f"la nota final es {estudent["notaFinal"]}\n")

# ---- actualizar --- 
def actualizar():
    
    try:
        actualizar_nombre = input("ingrese el nombre del estudiante a actualizar: ")
        for estudent in estudiantes:
            if estudent["nombre"] == actualizar_nombre:
                nuevo_nombre = input("ingrese el nuevo nombre: ")
                estudent["nombre"] = nuevo_nombre
                print("estudiante actualizado correctamente.")
                break
    except:
            print("estudiante no encontrado.")

# ---- eliminar ----
def eliminar():
    try:
        eliminar_nombre = input("ingrese el nombre del estudiante a eliminar: ")
        for i, estudent in enumerate(estudiantes):
            if estudent["nombre"] == eliminar_nombre:
                del estudiantes[i]
                print("estudiante eliminado correctamente.")
                break  
                
    except:
        print("estudiante no encontrado.")

# ---- guardar en archivo json ----
def guardar_en_archivo():
    json_data = json.dumps(estudiantes)
    with open("estudiantes.json", "w") as json_file:
        json_file.write(json_data)

    print("datos guardados en estudiantes.json")
#
def creardirectorio():
    nombre = input("Ingrese el nombre de la carpeta: ")
    valcsv = os.mkdir(nombre)
    os.listdir('.')
    print(valcsv)

ruta = os.path.join

def convertircsv():
    with open('estudiantes.json', 'r') as datos_json:
        datos = json.load(datos_json)

    dato = datos[0].keys()

    
    with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv,fieldnames= dato   )
        writer.writeheader()
        for i in datos:
            writer.writerow(i)

#----- menu -----
while True:
        print("1. Crear estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Guardar en archivo JSON")
        print("6. Guardar en archivo os")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

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
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
