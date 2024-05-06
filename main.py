import modules.corefile as cf
import funciones.globales as fg
import funciones.medicos as gf
import funciones.pasiente as fp
import funciones.consultas as cs
import ui.uiconsultas as uui
def mainmenu(op):
  fg.borrar_pantalla()
  title = """
    **************************
    * REGISTROS MEDICOS  *
    **************************
    """
  mainmenuOp = "1  historial \n2. tipos de medico \n3. datos de pasientes \n4. consultas \n5. salir"
  if (op !=5):
        print(title)
        print(mainmenuOp)
        try:
           opcion = int(input(''))
        except ValueError:
           input('ingresar opciones incorrects')
           fg.pausar_pantalla()
           mainmenu(0)
        else:
            match(opcion):
                case 1:
                    uui.Menumedicos(0)
                case 2:
                    gf.Newmedicos()
                case 3:
                    fp.NewPasientes()
                case 4:
                    cs.Newconsultas()
                case 5 :
                    print('hastala vista bb')
                case _:
                    print('opcion no validad en el menu')
                    fg.pausar_pantalla
                    mainmenu(0)      
if __name__ == "__main__":
    cf.MY_DATOS = "data/json"
    cf.checkfile(fg.camperye)
    mainmenu(0) 
