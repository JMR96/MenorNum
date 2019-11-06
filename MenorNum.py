# -*- coding: latin1 -*-

print('Insira 3 Numeros Inteiros diferentes.')
a = int(input('Insira o Primeiro Valor: '))
b = int(input('Insira o Segundo Valor: '))
c = int(input('Insira o Terceiro Valor: '))

if  (a < b) and (a < c):
    print('O Primeiro Valor eh o menor: %d' % a)
elif    (b < a) and (b < c):
    print('O Segundo Valor eh o menor: %d' % b)
elif    (c < a) and (c < b):
    print('O Terceiro Valor eh o menor: %d' % c)
else:
    print ('Valores nao especificados corretamente ou existem valores iguais')
