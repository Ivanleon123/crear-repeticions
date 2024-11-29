def crear_repetits(n, caracter):
    """Retorna el caràcter repetit n vegades."""
    return caracter * n

# Proves de la funció
print(crear_repetits(5, "a"))  # Retorna "aaaaa"
print(crear_repetits(3, "*"))   # Retorna "***"
print(crear_repetits(0, "x"))   # Retorna ""
print(crear_repetits(2, "Hola")) # Retorna "HolaHola"