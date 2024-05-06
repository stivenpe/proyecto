import os
import json
import funciones.globales as gf
import modules.corefile as  cf
import main


def NewPasientes():
    title = """
    **************************
    * REGISTRAR PACIENTE    *
    **************************
    """
    
    gf.borrar_pantalla()
    print(title)
    identificacion = input("ingrese la identificacion : ")
    nombre_apellido = input("ingrese nombre y apellido : ")
    telefonico = input("ingrese el numero telefonico : ")
    celular = input("ingrese el numero de celular  : ")
    fecha = input("ingrese la fecha de nacimiento : ")
    edad =  input("ingrese la edad : ")
    genero = input("ingrese el genero : ")
    pacientes = {
        "indentificacion" : identificacion,
        "nombre_apellido " : nombre_apellido,
        "telefonico" :  telefonico,
        "celular" : celular,
        "fecha" :   fecha, 
        "edad"   : edad,  
        "genero " : genero,
        
        "fecha" :     {
        "dia" : {},
        "mes" : {},
        "año" : {}
        }
    }   
    cf.addData('data',identificacion,pacientes)
    gf.camperye.get('data')
    if(bool(input('desea ingresar otro pasiente s(si) o (no)enter'))):
      NewPasientes(0)
    else :
        main.mainmenu(0)  
