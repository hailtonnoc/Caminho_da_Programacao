a = int(input('Qual o primeiro valor? '))
b = int(input('Qual o primeiro valor? '))
c = int(input('Qual o primeiro valor? '))
#VERIFICADOR DE MAIOR
if a>b and a>c:
    maior = a
if  b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#VERIFICADOR DE MENOR
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print(maior)
print(menor)