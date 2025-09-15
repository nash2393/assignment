def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
