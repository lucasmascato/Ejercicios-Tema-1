from typing import List

def calcula_imc_2(peso, altura):
    imc = peso / altura**2
    return imc

def calcula_estado_nutricional_2(peso, altura):
    imc = calcula_imc_2(peso, altura)
    if imc < 18:
        return("Bajo peso")
    elif 18.5 <= imc < 25:
        return("Normal")
    elif 25 <= imc < 30:
        return("Sobrepeso")
    else: 
        return("Obesidad")  
     
def imprime_estados_nutricionales(lista):
    for i in range(len(lista)):
        peso = lista[i][0]
        altura = lista[i][1]
        print(f'El IMC de la persona {i} es: {calcula_imc_2(peso, altura)} y su estado nutricional es: {calcula_estado_nutricional_2(peso, altura)}')
