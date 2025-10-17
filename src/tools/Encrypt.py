from utils.Shifts import shifts
from utils.Spinner import with_spinner

@with_spinner("Encriptando...")
def encrypt(i_file_path: str, o_file_path: str, shift_values: list[int], alphabet: list[str]) -> None:
    with open(i_file_path, 'r') as f:
        data = f.read()

    alphabet_shifted = alphabet.copy()

    for shift in shift_values:
        alphabet_shifted = shifts(shift, alphabet_shifted)
    
    table = str.maketrans(''.join(alphabet), ''.join(alphabet_shifted))
    encrypted_data = data.translate(table)
    with open(o_file_path, 'w') as f:
        f.write(encrypted_data)
    