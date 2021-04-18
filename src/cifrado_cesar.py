"""
Uso: Cifrar informacion con cesar
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 17 Abril 2020
"""

message = input('Ingresa el mensaje: ')
espacios = 1
while espacios > 0:
    clave = input('Ingresa tu palabra clave para cifrar: ')
    espacios = clave.count(' ')
    if clave.isalpha() == False:
        espacios += 1
key = len(clave)

