def apply_discount(amount):
    if amount < 0:
        raise ValueError("El monto no puede ser negativo")
    if amount > 1000:
        return amount * 0.85
    return amount