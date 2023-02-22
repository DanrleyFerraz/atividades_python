"""
Exercício sobre funções

Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro. 

"""

# -------------- Calculo duplicando --------------

def duplicar(operacao):
    def duplicando(numero):
        resultado = numero*2
        return f'A operação foi {operacao}, o número digitado foi {numero} e o resultado foi {resultado}'
    return duplicando

#                                \/Aqui é para informar o que será mostrado na parte do 'A operação foi...'
calculo_duplicando = duplicar('Duplicar')

#                       \/ Necessário que seja informado um valor para ser realizado o cálculo.
print(calculo_duplicando(2))

# -------------- Calculo triplicando --------------

def triplicar(operacao):
    def triplicando(numero):
        resultado = numero*3
        return f'A operação foi {operacao}, o número digitado foi {numero} e o resultado foi {resultado}'
    return triplicando

calculo_triplicando = triplicar('Triplicar')

print(calculo_triplicando(22))

# -------------- Calculo quadruplicando --------------

def quadruplicar(operacao):
    def quadruplicando(numero):
        resultado = numero*4
        return f'A operação foi {operacao}, o número digitado foi {numero} e o resultado foi {resultado}'
    return quadruplicando

calculo_quadruplicando = quadruplicar('Quadruplicar')

print(calculo_quadruplicando(60))