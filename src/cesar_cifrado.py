"""
Uso: Cifrar informacion con cesar
Creado: Andrés Hernández Mata
Version: 1.1.0
Python: 3.9.1
Fecha: 17 Abril 2020
"""

import os

os.system("cls")

def Encriptar(Frase):
    FraseEnc = '' #str vacio
    for letra in Frase: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    return FraseEnc

