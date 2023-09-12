def calculadora(n1, n2, operador):
    soma = n1 + n2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        return num1 / num2
    else:
        return 0


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operador = int(input('Digite o número correspondente ao operador -> 1.soma; 2.subtração; 3.multiplicação; 4.divisão: '))

resultado = calculadora(num1, num2, operador)
print(resultado)