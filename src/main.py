import argparse
import os
import re
from utils.Config import load_config
from tools.Encrypt import encrypt
from tools.Decrypt import decrypt

config = load_config()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cifrado César con parámetros configurables.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', action='store_true', help='Encripta el archivo de entrada')
    group.add_argument('-d', action='store_true', help='Desencripta el archivo de entrada')
    parser.add_argument('-s', type=str, help='Numero de veces a encriptar + desplazamiento: "[#,#,#]" o "[#]"')
    parser.add_argument('-i', type=str, required=True, help='Recibe el archivo de entrada')
    parser.add_argument('-o', type=str, help='Archivo de salida (Por defecto el mismo que la entrada + "-encripted")')
    parser.add_argument('-c', action='store_true', help='Recarga los parametros del archivo params.conf (Por defecto esta activado)')

    args = parser.parse_args()

    if args.c:
        config = load_config()
        print("Configuración recargada desde params.conf")
        exit(0)

    input_file = os.path.abspath(args.i)
    output_file = os.path.abspath(args.o) if args.o else f"{os.path.splitext(input_file)[0]}-{'encripted' if args.e else 'desencripted'}{os.path.splitext(input_file)[1]}"

    s, shifts = 1, [3] # Valores por defecto

    if args.s:
        pattern = r'^\[(?P<shifts>(-?\d+,?)+)\]$'
        match = re.match(pattern, args.s)
        if match:
            shifts = list(map(int, match.group('shifts').split(',')))
            s = len(shifts)
        else:
            print("Formato inválido para el parámetro -s. Use el formato \"[#,#,#]\" o \"[#].\"")
            exit(1)

    # obtain alphabet and ensure it's not None
    alphabet = config.get_alphabet()
    if alphabet is None:
        print("Alfabeto no configurado en params.conf")
        exit(1)

    if args.e:
        print(f"Encriptando {input_file.split('/')[-1]} a {output_file.split('/')[-1]} con {s} veces y desplazamientos {shifts}")
        encrypt(input_file, output_file, shifts, alphabet)

    if args.d:
        print(f"Desencriptando {input_file.split('/')[-1]} a {output_file.split('/')[-1]} con {s} veces y desplazamientos {shifts}")
        decrypt(input_file, output_file, shifts, alphabet)


    print("Operación completada.")
