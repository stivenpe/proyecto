import os
import json
import funciones.globales as gf
import modules.corefile as  cf
import ui.uiconsultas as uui
def Newconsultas():

    title = """
    **************************
    * REGISTRAR CONSULTAS    *
    **************************
    """
    
    gf.borrar_pantalla()
    print(title)
    id_medico=input("ingresa la id medico : ")
    id_paciente=input("ingrese la id de pacientes : ")
    fecha=input("ingrese la fecha : ")
    diagnostico=input("ingrese el diagnostico : ")
    tratamiento=input("ingrese el tratamiento :")

    consulta = {
        'id_medico': id_medico,
        'id_paciente': id_paciente,
        'fecha': fecha,
        'diagnostico': diagnostico,
        'tratamiento': tratamiento
    }
    cf.addData('data',id_medico,consulta)
    gf.camperye.get('data')
    if(bool(input('desea ingresar otro consultas s(si) o (no)enter :'))):
        Newconsultas()
    else :
        uui.Menumedicos(0)

def SearchData():
   criterio = input('ingrese el numero de indentificacion del pasiente :')
   data=gf.camperye.get("data").get(criterio)
   return data

def Modifydata():
    dataconsul = SearchData()
    id_medico,id_paciente,fecha,diagnostico,tratamiento=dataconsul.values()
    for key in dataconsul.keys():
        if(key !="identificacion" and key != "tratamiento"):
            if(bool(input(f'desea modificar el {key} s(si) o (no)enter'))):
                dataconsul[key]=input(f"ingresa el nuevo valor para {key} :")
    gf.camperye.get('data')
    cf.updatefile(gf.camperye)
    uui.Menumedicos(0)
