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

os.system("cls")

if __name__ == "__main__":

    description = """Example -modo e -mensaje 'Hola Mundo' -clave 3 """
    parser = argparse.ArgumentParser(description='Cifrado cesar', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-modo", metavar='--modo', dest="modo", help="Modo para encriptar, desencriptar o hackear", required=True)
    parser.add_argument("-mensaje", metavar='--mensaje', dest="mensaje", help="Mensaje para cifrar, desencriptar o para hackear", required=True)
    parser.add_argument("-clave", metavar='--clave', dest="clave", help="Clave para cifrar o descifrar el mensaje", default = "3")
    params = parser.parse_args()


def cifrar(mensaje):
    frase = ''
    for letra in mensaje:
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                frase += y
                encontrado = True
        if not encontrado:                            
            frase += letra
    return frase

def desencriptar(mensaje):
    frase = ''
    for letra in mensaje:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                frase += x
                encontrado = True
        if not encontrado:
            frase += letra
    return frase

abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}