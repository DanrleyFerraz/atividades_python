
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da variável

def multiplicacao(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

resultado_final = multiplicacao(1,2,3,4)
print(resultado_final)


# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar.

def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(impar_par(2))
print(impar_par(3))
print(impar_par(5))
print(impar_par(7))

