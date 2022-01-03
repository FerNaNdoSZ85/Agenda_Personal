
#!  DECLARACION DE FUNCIONES Y VERIFICACIONES
from var_y_func import cfg_vyf

def es_valido(valor, SELECCIONA):
    return valor.isdigit() and int(valor) in SELECCIONA.keys()

def selecciona_del_menu(SELECCIONA):
    print ('Seleccione una accion: ')
    for key, value in SELECCIONA.items():
        print("%s - %s" % (key, value["accion"]))

    opcion = input('\nINGRESE OPCION: ')
    
    while not es_valido(opcion, SELECCIONA):
        print ('SELECCION INCORRECTA, REINTENTE')
        opcion = input('\nINGRESE OPCION: ')
    return int(opcion)