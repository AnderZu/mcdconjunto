
# escribir el codigo de main para ingresar n numero naturales y calcular em MCD de los numeros ingresados
if __name__ == '__main__':
from src.logica.OperacionesEnteros import OperacionesEnteros

    cantidadNumero = int(input("ingrese cantidad de numeros: "))
    numero = []
    for x in range(0, cantidadNumero):
        numero.append(int(input("ingrese valor: ")))
    print(numero)
    resultadoMCD = self.MCDMasDosNumeros()
print(f"el MCD de {cantidadNumero} numeros los cuales son {numero} es {resultadoMCD}")

