import json
import csv

def cargar_mascotas():
    try:
        with open('mascotas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_mascotas(mascotas):
    with open('mascotas.json', 'w') as archivo:
        json.dump(mascotas, archivo, indent=4)

def registrar_mascota():
    mascotas = cargar_mascotas()
    
    codigo = input("Ingrese el codigo de la mascota: ") #
    
    if codigo in mascotas:
        print("Ya existe una mascota con ese codigo.")
        return

    nombre = input("Nombre: ") 
    especie = input("Especie: ") 
    raza = input("Raza: ")
    fecha_nac = input("Fecha de nacimiento: ") 
    propietario = input("Nombre del propietario: ") 
    telefono = input("Telefono: ") 
    estado = input("Estado (activo/inactivo): ").lower()

    mascotas[codigo] = {
        "Nombre": nombre,
        "Especie": especie,
        "Raza": raza,
        "Fecha de nacimiento": fecha_nac,
        "Nombre del propietario": propietario,
        "Telefono": telefono,
        "Estado": estado
    }
    
    guardar_mascotas(mascotas)
    print("Mascota guardada.")

def mostrar_mascotas():
    mascotas = cargar_mascotas()
    
    if len(mascotas) == 0:
        print("No hay mascotas.")
    else:
        for codigo, datos in mascotas.items():
            print(f"Codigo: {codigo} - Nombre: {datos['Nombre']} - Propietario: {datos['Nombre del propietario']}")

def buscar_mascota_por_codigo():
    codigo = input("Ingrese el codigo a buscar: ") 
    mascotas = cargar_mascotas()
    
    if codigo in mascotas:
        datos = mascotas[codigo]
        print(f"Nombre: {datos['Nombre']}")
        print(f"Especie: {datos['Especie']}")
        print(f"Propietario: {datos['Nombre del propietario']}")
        print(f"Estado: {datos['Estado']}")
    else:
        print("Mascota no encontrada.")

def registrar_consulta():
    mascotas = cargar_mascotas()
    cod_mascota = input("Ingrese el codigo de mascota: ") 
    
    if cod_mascota not in mascotas:
        print("La mascota no existe.")
        return

    cod_consulta = input("Codigo de consulta: ") 
    fecha = input("Fecha: ") 
    motivo = input("Motivo: ") 
    diagnostico = input("Diagnostico: ") 
    tratamiento = input("Tratamiento: ") 
    costo = input("Costo: ") 

    try:
        with open('consultas.csv', 'x', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Codigo de consulta", "Codigo de mascota", "Fecha", "Motivo", "Diagnostico", "Tratamiento", "Costo"]) 
    except FileExistsError:
        pass

    with open('consultas.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([cod_consulta, cod_mascota, fecha, motivo, diagnostico, tratamiento, costo])
    
    print("Consulta guardada.")