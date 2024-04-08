from lib.Suma import Suma

if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
segundoSumando = int(input("Ingrese segundo sumando: "))
suma = Suma(primerSumando, segundoSumando)
print(f"{primerSumando} + {segundoSumando} = {suma.CalcularSuma()}")
