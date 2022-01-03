
#! PROGRAMA PRINCIPAL AGENDA
import os
from var_y_func.cfg_vyf import *
from cfg_menu_opc.cfg_menu_prin import MENU_OPC
from modulo_datos import datos


exit = False
while not exit:
    #os.system('cls')
    print('Bienvenido a su Agenda Personal')
    print('*******************************')
    print('|| -= ReMake by FerNaNdo =-  ||')
    print('******************************* \n')
    selecciona = selecciona_del_menu(MENU_OPC)
    getattr(datos, MENU_OPC[selecciona]["accion"])()