import random


nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10

resultado_digito_1 = 0 

for numeros in nove_digitos:
    resultado_digito_1 += int(numeros)*contador_regressivo_1
    contador_regressivo_1 -= 1


numeros = (resultado_digito_1*10) % 11

if numeros > 9:
    digito_1 = 0

else: 
    digito_1 = numeros

 
dez_digitos = nove_digitos + str(digito_1)

contador_regressivo = 11

resultado_digito_2 = 0

for numeros in dez_digitos:
    resultado_digito_2 += int(numeros) * contador_regressivo
    contador_regressivo -= 1

resultado_numeros = (resultado_digito_2*10) % 11

if resultado_numeros > 9:
    digito_2 = 0

else:
    digito_2 = resultado_numeros



cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'



print(f'O CPF gerado foi: {cpf_gerado_pelo_calculo}')

for i in range(20):
    print('\t')




