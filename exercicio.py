nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

nome_invertido = nome[::-1] #CASO PRECISE DE GAMBIARRA 
nome_check = nome[0:1:1] #CASO PRECISE DE GAMBIARRA

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    

    if ' ' in nome:
        print('Seu nome contém espaços')
    
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Você deixou algum dos campos em branco.')
#if ' ' in nome and idade:
  #  print('Desculpe, você deixou campos vazios.')
