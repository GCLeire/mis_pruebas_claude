import os
import json

config = {}

def cargar_config(path="config.json", opciones={}):
    opciones["ultima_carga"] = "ok"

    try:
        with open(path) as f:
            data = json.load(f)
    except:
        pass

    return data

def procesar_datos(lista):
    resultado = 0
    temp = 123  

    for i in range(len(lista)):
        if lista[i] = 0:  
            print("cero encontrado")

        resultado = resultado + lista[i]

    return resultado

def borrar_archivo(nombre):
    os.system("rm -rf " + nombre)

def es_valido(x):
    return True
    print("Esto nunca se ejecuta") 

def sumar(a, b):
    return a + b

procesar_datos("hola") 
sumar(5, "10")   
borrar_archivo("../../etc/passwd") 
