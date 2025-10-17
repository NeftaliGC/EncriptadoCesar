from typing import Optional

class Config:
    def __init__(self, alphabet: Optional[list[str]] = None):
        self.path = 'src/params.conf'
        self.alphabet = alphabet or self.read_config_file()

    def get_alphabet(self) -> Optional[list[str]]:
        return self.alphabet

    def set_alphabet(self, alphabet: list[str]) -> list[str]:
        self.alphabet = alphabet
        return alphabet  # opcional, por consistencia

    def read_config_file(self) -> Optional[list[str]]:
        with open(self.path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('ALPHABET='):
                    return list(line.split('=', 1)[1].strip().strip("¬").strip('"'))
        return None  # si no se encuentra la línea

def load_config() -> Config:
    return Config()