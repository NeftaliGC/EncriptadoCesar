
def shifts(d: int, l: list[str]) -> list[str]:
    n = len(l)
    d = d % n  # Asegura que el desplazamiento esté dentro del rango de la lista
    return l[d:] + l[:d]