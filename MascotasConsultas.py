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