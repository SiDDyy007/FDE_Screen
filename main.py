def sort(width, height, length, mass):
    if not all(isinstance(x, (int, float)) and x >= 0 for x in [width, height, length, mass]):
        raise ValueError("Dimensions and mass must be non-negative numbers")

    volume = width * height * length

    is_bulky = (
        volume >= 1000000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
