
#! MODULO DE MODIFICACION DE DATOS
import sys
import os

AGENDA= []
PAPELERA =[]
contacto_ ={}
encontrados=[]
recuperar = 0
alguien = ''
buscado =''
i=0
def SALIR():
    print('EL PROGRAMA HA TERMINADO')
    sys.exit()

def nombre():
    nom = input('Ingrese Nombre/s: ')
    return nom

def apellido():
    ape = input('Ingrese Apellido/s: ')
    return ape

def dire():
    dir = input('Ingrese Direccion: ')
    return dir
def tel():
    telef = input('Ingrese Telefono: ')
    return telef
def email():
    corr = input('Ingrese email: ')
    return corr

def AGREGAR_CONTACTO():
    contacto_ = {
    "Nombre" : nombre().capitalize(), 
    "Apellido" : apellido().capitalize(),
    "Direccion" : dire().capitalize(),
    "Telefono" : tel(),
    "E-Mail" : email()}
    AGENDA.append(list(contacto_.values()))

def eliminar(quitar):
    PAPELERA.append(AGENDA[quitar-1])
    AGENDA.pop(quitar-1)
    print('==> Contacto Eliminado <== ')

def ELIMINAR_CONTACTO():
    LISTAR_CONTACTOS()
    print('************************************')
    quitar = int(input('SELECCIONE N° DE CONTACTO A ELIMINAR: '))
    ind_=[]
    for i in range(len(AGENDA)):
        ind_.append(i+1)
    if quitar in ind_:
        eliminar(quitar)
    else:
        print('N° NO VALIDO')

def LISTAR_CONTACTOS():
    print("{:<4}{:^20}{:^20}{:^20}{:^20}{:^20}".format("N°","NOMBRE","APELLIDO","DIRECCION","TELEFONO","EMAIL"))
    c=0
    for ListC in AGENDA:
        print('{:<3}'.format(c+1), "{:^20}{:^20}{:^20}{:^20}{:^20}".format(ListC[0],ListC[1],ListC[2],ListC[3],ListC[4]))
        c += 1

def VER_PAPELERA():
    si_o_no = ""
    print("{:^3} {:^20} {:^20} {:^20} {:^20} {:^20}".format("N°","NOMBRE","APELLIDO","DIRECCION","TELEFONO","EMAIL"))
    c=0
    for EliC in PAPELERA:
        print('{:<3}'.format(c+1), "{:^20}{:^20}{:^20}{:^20}{:^20}".format(EliC[0],EliC[1],EliC[2],EliC[3],EliC[4]))
        c+=1

    if len(PAPELERA) > 0:
        si_o_no = input('Recuperar algun contacto? ==> S/N: ').upper()
        if si_o_no== "S" or si_o_no == "N":
            recuperar = int(input('-= Teclee N° =-: '))
            ind_=[]
            for i in range(len(PAPELERA)):
                ind_.append(i+1)
            if recuperar in ind_:
                RECUPERAR(recuperar)
            else:
                print('N° NO VALIDO')
    else:
        print('PAPELERA VACIA MAN')


def RECUPERAR(recuperar):
    AGENDA.append(PAPELERA[recuperar-1])
    PAPELERA.pop(recuperar-1)
    print(PAPELERA)

