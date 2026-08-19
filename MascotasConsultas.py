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