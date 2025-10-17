# Cifrado César de archivos de texto

## Caracteristicas
Utiliza como mapa de caracteres:
- Mayusculas
- Minusculas
- Caracteres Especiales

## Parametros del programa
- `-e` Encripta el archivo de entrada
- `-d` Desencripta el archivo de entrada
- `-r` Numero de veces a encriptar + desplazamiento: [#,#,#] o [#] donde # es el desplazamiento y el numero es las veces que se repite la operacion
- `-i` Recibe el archivo de entrada
- `-o` Archivo de salida (Por defecto el mismo que la entrada + "-encripted")
- `-c` Recarga los parametros del archivo `params.conf` (Por defecto esta activado)

## Ejemplo de uso
```bash
python3 src/main.py -e -r [1,2] -i input.txt -o output.txt
```