from ejercicio1 import *
def calcula_estado_nutricional(Usuario):
    imc = calcula_imc(Usuario)
    if imc < 18:
        print("Bajo peso")
    elif 18.5 <= imc < 25:
        print("Normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    else: 
        print("Obesidad")  