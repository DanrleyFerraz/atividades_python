############################ VALIDAÇÃO DO PRIMEIRO DIGITO ############################

cpf_enviado_usuario = '74682489070'


nove_digitos = cpf_enviado_usuario[:9]
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

############################ VALIDAÇÃO DO PRIMEIRO DIGITO CONCLUIDA ############################

################## ABAIXO DISSO JÁ COMEÇA A VALIDAÇÃO DO SEGUNDO DIGITO ##################

############################ VALIDAÇÃO DO SEGUNDO DIGITO ############################

dez_digitos = cpf_enviado_usuario[:10]

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

############################ VALIDAÇÃO DO SEGUNDO DIGITO CONCLUIDA ############################


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'O CPF {cpf_enviado_usuario} É VALIDO!')

else:
    print('CPF INVALIDO!')



