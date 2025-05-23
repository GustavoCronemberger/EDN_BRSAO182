def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def modulo(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a % b