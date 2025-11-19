def calcula_imc(Usuario):
    while True:
        try:
            peso = float(input('Introduzca su peso en kilogramos: '))
            altura = float(input('Introduzca su altura en metros (Utilice un punto decimal si es necesario):'))
        except ValueError:
            print('Valor incorrecto: Introduzca un número válido.')
            continue
        if altura <= 0:
            print('Valor incorrecto: Introduzca un número psoitivo para la altura.')
            continue
        if peso <= 0:
            print('Valor incorrecto. Introduzca un número positivo para el peso.')
            continue
        break
    imc = peso / altura**2
    print(f"El IMC de {Usuario if Usuario else 'usuario'} es : {imc:.2f}")
    return imc