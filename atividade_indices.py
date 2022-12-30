"""

Exercício

Exiba os índices da lista

0 Maria
1 Helena
2 Luiz

"""

lista = ['Maria', 'Helena', 'Luiz', 'Celso', 'Jorge', 'Arlindo', 'David']

lista.append('Melqui')
lista.append('Mika')
lista.append('Michael')
lista.append('Douglas')
lista.append('Rhuan')
lista.append('Everlandy')

indice = 0

for nome in lista:
    indice += 1
    print(indice, nome)