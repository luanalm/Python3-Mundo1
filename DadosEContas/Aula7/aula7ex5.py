# Exercício 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Conversor de valor de metros para centímetros e milímetros')
x = int(input('Valor em metros: '))

c = x * 100
m = x * 1000

print('O valor em é igual {} centímetros e {} milímetros'.format(c, m))
