import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesEnteros()
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCDRecursivo_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 15
        numero2 = 20
        resultadoEsperado = 5
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = self.operacion.MCD_recursivo(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCDRecursivo_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 15
        numero2 = 20
        numero3 = 30
        resultadoEsperado = 5
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = self.operacion.MCD_recursivo(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCDRecursivo_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 15
        numero2 = 20
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 5
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = self.operacion.MCD_recursivo(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)