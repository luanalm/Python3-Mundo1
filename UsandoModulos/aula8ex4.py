# Exercício 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')

x = random.randint(1,4)

if x == 1:
    print('O aluno escolhido foi {}!'.format(a))
elif x == 2:
    print('O aluno escolhido foi {}!'.format(b))
elif x == 3:
    print('O aluno escolhido foi {}!'.format(c))
else:
    print('O aluno escolhido foi {}!'.format(d))