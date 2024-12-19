
# par ou impar
nome = (input('Digite seu nome: '))
num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'Olá {nome}! O número {num} digitado é par.')
else:
    print(f'Olá {nome}! O número {num} digitado é ímpar.')

# Media dos alunos
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f'A média do aluno foi: {media:.2f}')

# Verificar palíndromo
palavra = input('Digite um palavra: ')
if palavra == palavra[::-1]:
    print(f'A palavra {palavra} é um palíndromo.')
else:
    print(f'A palavra {palavra} não é um palíndromo.')

# Tabuada
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11):
    print(f'{num} x {i} = {num * i}')

# Fatorial de um número
numero = int(input('Digite um número: '))
fatorial = 1

for i in range (1, numero + 1):
    fatorial *= i

print(f'O fatorial de {numero} é {fatorial} ')

# Maior de 3 
num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))

maior = max(num1, num2, num3)
print(f'O maior número é {maior}.')

# Contador de vogais
frase = input('Digite uma frase: ')
vogais = 'aeiou'
contador = 0
# A&M is a great place to start your career in IT.
for letra in frase:
    if letra in vogais:
        contador += 1

print(f'O número de vogais é: {contador}')

# Inversão de strings
texto = input('Digite um texto: ')
inversao = texto[::-1]
print(f'Texto invertido: {inversao}') 

# número primo
numero = int(input('Digite um num: '))
primo = True

for i in range (2,numero):
    if numero % i == 0:
        primo = False

if primo == 1:
    print(f'o num {numero} é primo.')
else:
    print(f'o num {numero} não é primo.')

#contador de letras 
n = input('Digite o seu nome completo: ').lower()
letras = 'abcdefghijklmnopqrstuvwxyz'
contador = 0

for letra in n:
    if letra in letras:
        contador +=1

print(f'Seu nome tem {contador} letras')