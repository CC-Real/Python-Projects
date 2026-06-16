def main():
    value = input("What would you like to input for your expression? ")
    x, y, z = value.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    print(f"{result:.1f}")
main()
