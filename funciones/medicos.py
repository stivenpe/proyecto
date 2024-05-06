import os
import json
import funciones.globales as gf
import modules.corefile as  cf
import main

def Newmedicos ():
    title = """
    **************************
    * REGISTRAR MEDICOS    *
    **************************
    """
    
    gf.borrar_pantalla()
    print(title)
    tiposdemedico = input ("ingrese el tipo de especialista :")
    indentificacion = input("ingrese la identificacion : ")
    nombre_apelledo = input("ingrese nombre y apellido : ")
    correo_electronico = input("ingrese el correo electronico : ")
    numero_de_consultorio= input("ingrese el numero de consultorio  : ")
    horario_de_atencion = input("ingrese el horario de atencion : ")
    
    medicos = {
        "tiposdemedico" : tiposdemedico,
        "indentificacion" : indentificacion,
        "nombre_apellido " : nombre_apelledo,
        "correo_electronico" : correo_electronico, 
        "numero_de_consultorio" : numero_de_consultorio,
        "horario_de_atencion " : horario_de_atencion,
        "horario" :
            {
            "mañana" : {},
            "tarde" : {}
        } 
        
    }  
    cf.addData("data",indentificacion,medicos)
    gf.camperye.get("data")
    if(bool(input('desea ingresar otro especialista s(si) o enter(no)'))):
     Newmedicos(0)
    else :
        main.mainmenu(0)
       