import sys


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def validar_numeros(args):
    if len(args) != 3:
        print("Uso: python nombre_script.py <numero1> <numero2>")
        sys.exit(1)

    try:
        num1 = int(args[1])
        num2 = int(args[2])
        return num1, num2
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        sys.exit(1)


def main():
    num1, num2 = validar_numeros(sys.argv)
    resultado = mcd(num1, num2)
    print("El MCD de", num1, "y", num2, "es:", resultado)


if __name__ == "__main__":
    main()
