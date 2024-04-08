from Suma import Suma

if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
segundoSumando = int(input("Ingrese segundo sumando: "))
suma = Suma()
print(f"{primerSumando} + {segundoSumando} = {suma.CalcularSuma(primerSumando, segundoSumando)}")
