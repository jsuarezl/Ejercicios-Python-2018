import os
import traceback

from ejercicios import compañeros
from ejercicios import conjuntos
from ejercicios import conteobases as conteo
from ejercicios import tuplasvih as tuplas
from ejercicios.fracciones import Rational
from ejercicios.matrices import Matriz
from ejercicios.plano import Point
from ejercicios.plano import Rectangle


def instrucciones():
    try:
        ejercicio(checkint(input("""
        Por favor ingresa un número para ejecutar el ejercicio:
        1) Conteo de bases nitrogenadas.
        2) Coincidencia de edad y comuna en lista de diccionarios.
        3) Orden de tuplas de países y personas con VIH.
        4) Operaciones en conjuntos de Fibonacci y números primos.
        5) Manejo de fracciones.
        6) Rectangulos en el plano.
        7) Modulo de una matriz
        8) Salir del programa.


        Ejercicio a ejecutar: """)))
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        print("Error desconocido", e)
        traceback.print_exc()


def ejercicio(numero):
    if numero == 1:
        conteo.levadura(os.path.join(os.path.dirname(__file__), 'res', 'Gen_Levadura.txt'))
    elif numero == 2:
        compañeros.conteo()
    elif numero == 3:
        tuplas.tuplas()
    elif numero == 4:
        conjuntos.conjuntos()
    elif numero == 5:
        fr = [Rational(1, 2), Rational(5, 9), Rational(14, 5)]
        print("Racionales a operar y representar: ")
        for x in fr:
            print(x)
        for x in fr:
            try:
                n = checkint(input('Ingresa el numerador para operar {}: '.format(x)))
                m = checkint(input('Ingresa el denominador para {}: '.format(n)))
                if n == 0 or m == 0:
                    print("El numerador y denominador deben ser enteros diferentes de 0.")
                    exit(3)
                r = Rational(n, m)
                try:
                    print(x, ' + ', r, ' = ', x.plus(r), ' = ', x.plus(r).value())
                except ValueError as e:
                    print(e)
                try:
                    print(x, ' - ', r, ' = ', x.minus(r), ' = ', x.minus(r).value())
                except ValueError as e:
                    print(e)
                try:
                    print(x, ' * ', r, ' = ', x.times(r), ' = ', x.times(r).value())
                except ValueError as e:
                    print(e)
                try:
                    print(x, ' / ', r, ' = ', x.divides(r), ' = ', x.divides(r).value())
                except ValueError as e:
                    print(e)
            except Exception as e:
                print(e)
                continue
    elif numero == 6:
        rect1 = Rectangle(Point(10, 5), Point(15, 10))
        rect2 = Rectangle(Point(checkint(input('Ingresa un valor para \'x1\' de \'rect2\': ')),
                                checkint(input('Ingresa un valor para \'y1\' de \'rect2\': '))),
                          Point(checkint(input('Ingresa un valor para \'x2\' de \'rect2\': ')),
                                checkint(input('Ingresa un valor para \'y1\' de \'rect2\': '))))
        print('Rectángulos a usar:\n'
              ' rect1: {}\n'
              ' rect2: {}'.format(rect1, rect2))
        print('Área rect1: {}, Área rect2: {}'.format(rect1.area(), rect2.area()))
        print('Solapados: ', rect1.solapado(rect2))
        print('Área de intersección: {}'.format(
            rect1.interseccion(rect2).area() if rect1.solapado(rect2) else 'No están solapados'))
        print('Rectángulo desde la intersección: {}'.format(
            rect1.interseccion(rect2) if rect1.solapado(rect2) else 'No están solapados'))
    elif numero == 7:
        m = Matriz(6, 6,
                   [1, 2, 3, 4, 5, 4, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0, 9, 2, 0, 3, 6, 3, 12, 6, 8, 9, 6, 8, 9, 3, 4, 5, 6,
                    7, 2, 3])
        print("Determinante: {}".format(m.determinante()))
        print("Matriz 1:\n{}".format(m))
        suma = m.plus(m)
        print("Determinante de la suma: {}".format(suma.determinante()))
        print("Matriz de la suma: \n{}".format(suma))
        mult = m.times(m)
        print("Multiplicación: \n{}".format(mult))
        div = m.divides(m)
        print("División: \n{}".format(div))
    elif numero == 8:
        exit(0)
    else:
        print("Has ingresado un valor inválido.")
        exit(1)


def checkint(x):
    try:
        return int(x)
    except ValueError:
        print("No has ingresado un número válido")
        exit(1)


if __name__ == '__main__':
    instrucciones()
