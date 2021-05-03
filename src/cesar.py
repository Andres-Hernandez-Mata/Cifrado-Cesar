"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 02 Mayo 2020
"""

import argparse
import os
from datetime import datetime

def main():
    os.system("cls")
    print(datetime.now(), "\033[0;32m [INFO] Iniciando... \033[0;0m")
    description = """Example -modo e -mensaje 'Hola Mundo' -clave 3 \nExample -modo h -mensaje 'Hola Mundo' -clave 3 \nExample -modo d -mensaje 'Hola Mundo'"""
    parser = argparse.ArgumentParser(description='Cifrado cesar', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-modo", metavar='--modo', dest="modo", help="Modo para e (encriptar), d (desencriptar) o h (hackear)", required=True)
    parser.add_argument("-mensaje", metavar='--mensaje', dest="mensaje", help="Mensaje para cifrar, desencriptar o para hackear", required=True)
    parser.add_argument("-clave", metavar='--clave', dest="clave", help="Clave para cifrar o descifrar el mensaje, default clave 3", default="3")
    params = parser.parse_args()
    
    if params.modo == 'e':
        print(datetime.now(), "\033[0;32m [INFO] Encriptando mensaje... \033[0;0m")
        cesar(params.mensaje,True,params.clave)
    elif params.modo == 'd':
        print(datetime.now(), "\033[0;32m [INFO] Desencriptando mensaje... \033[0;0m")
        cesar(params.mensaje,False,params.clave)
    else:
        print(datetime.now(), "\033[0;32m [INFO] Seleccione el modo correcto... \033[0;0m")

def cesar(mensaje,modo,clave):
    simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    resultado = ''
    try:
        for simbolo in mensaje:
            if simbolo in simbolos:
                indice_simbolo = simbolos.find(simbolo)
                # Encriptar
                if modo:
                    indice_nuevo = indice_simbolo + clave
                # Desencriptar
                elif not modo:
                    indice_nuevo = indice_simbolo - clave

                if indice_nuevo >= len(simbolos):
                    indice_nuevo = indice_nuevo - len(simbolos)
                elif indice_nuevo < 0:
                    indice_nuevo = indice_nuevo + len(simbolos)
                resultado = resultado + simbolos[indice_nuevo]
            else:
                resultado = resultado + simbolo
    except Exception as error:
        print(datetime.now(), "\033[0;91m [ERROR] Ha ocurrido un error")
        print(error)


if __name__ == "__main__":    
    main()

