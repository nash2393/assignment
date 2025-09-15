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


if __name__ == "__main__":
    # Quick test cases
    print(sort(100, 100, 100, 10))   # SPECIAL (volume = 1,000,000 → bulky)
    print(sort(200, 50, 50, 10))     # SPECIAL (dimension ≥ 150)
    print(sort(100, 100, 100, 25))   # SPECIAL (heavy only)
    print(sort(200, 200, 200, 25))   # REJECTED (both bulky & heavy)
    print(sort(50, 50, 50, 10))      # STANDARD (neither bulky nor heavy)
