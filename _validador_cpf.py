# Validador de CPF


import re
import sys

cpf_enviado_usuario = input('Digite algum CPF para verificar se é válido: ')
cpf_check = re.sub(
    r'[^0-9]',
    '',
    cpf_enviado_usuario
)

if cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario):
    print('Você enviou dados sequenciais.')
    sys.exit()
 
nove_digitos = cpf_check[:9]
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

######################################################################

dez_digitos = cpf_check[:10]

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

if cpf_gerado_pelo_calculo == cpf_check:
    print(f'O CPF {cpf_check} É VALIDO!')

else:
    print('CPF INVALIDO!')
