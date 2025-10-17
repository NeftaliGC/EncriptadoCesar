from utils.Shifts import shifts
from utils.Spinner import with_spinner

@with_spinner("Desencriptando...")
def decrypt(i_file_path: str, o_file_path: str, shift_values: list[int], alphabet: list[str]) -> None:
    with open(i_file_path, 'r') as f:
        data = f.read()

    # Invertir el desplazamiento total
    total_shift = -sum(shift_values)
    alphabet_shifted = shifts(total_shift, alphabet)

    # Crear tabla inversa de traducción
    table = str.maketrans(''.join(alphabet), ''.join(alphabet_shifted))
    decrypted_data = data.translate(table)

    with open(o_file_path, 'w') as f:
        f.write(decrypted_data)
