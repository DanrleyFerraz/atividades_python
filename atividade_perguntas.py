# Exercício - sistema de perguntas e respostas


# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

import os

print("Quanto é 2+2 ?")
print(
    "\nA)1" 
    "\nB)3"
    "\nC)4"
    "\nD)5" 
)
resposta_1 = input("\nDigite sua resposta: ")

if resposta_1 == "4":
    print("\nParabéns acertou memo 👍👍")
    input("Aperte enter para continuar...")
    os.system("cls")



else:
    print("\nErrado 👎👎👎")
    input("Aperte enter para continuar...")
    os.system("cls")

    
print("\nQuanto é 5*5 ?")
print(
    "\nA)25 "
    "\nB)55"
    "\nC)10"
    "\nD)51"
)

resposta_2 = input("\nDigite sua resposta: ")

if resposta_2 == "25":
    print("\nParabéns paizão. Você acertou memo 👍👍")
    input("Aperte enter para continuar...")
    os.system("cls")

else:
    print("\nErrado amigo. Errado. 👎👎👎")
    input("Aperte enter para continuar...")
    os.system("cls")


print("\nQuanto é 10/2 ?")
print(
    "\nA)4"
    "\nB)5"
    "\nC)2"
    "\nD)1"
)

resposta_3 = input("\nDigite sua resposta: ")

if resposta_3 == "5":
    print("\nParabéns paizão. Você acertou memo 👍👍")
    input("Aperte enter para continuar...")
    os.system("cls")

else:
    print("\nErrado amigo. Errado. 👎👎👎")
    input("Aperte enter para continuar...")
    os.system("cls")

if resposta_1 == "4" and resposta_2 == "25" and resposta_3 == "5":
    print("Você acertou 3 de 3 perguntas.")

elif resposta_1 != "4" and resposta_2 == "25" and resposta_3 == "5":
    print("Você acertou 2 de 3 perguntas.")

elif resposta_1 != "4" and resposta_2 != "25" and resposta_3 == "5":
    print("Você acertou 1 de 3 perguntas.")

elif resposta_1 != "4" and resposta_2 != "25" and resposta_3 != "5":
    print("Você acertou 0 de 3 perguntas.")

elif resposta_1 == "4" and resposta_2 != "25" and resposta_3 == "5":
    print("Você acertou 2 de 3 perguntas.")

elif resposta_1 == "4" and resposta_2 == "25" and resposta_3 != "5":
    print("Você acertou 2 de 3 perguntas.")

elif resposta_1 == "4" and resposta_2 != "25" and resposta_3 != "5":
    print("Você acertou 1 de 3 perguntas.")

elif resposta_1 != "4" and resposta_2 == "25" and resposta_3 != "5":
    print("Você acertou 1 de 3 perguntas.")
