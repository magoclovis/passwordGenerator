# import random, seed
import string
from random import choice

# strings já prontas, sem a necessidade de criar um vetor e encher de valores
string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.

# a primeira escolha terá um valor fora do while para retorná-lo e fazer parecer um menu 
# poderia ser feito usando switch case mas queria fazer de uma forma simples 
# É possivel adicionar mais senhas evitando com que o programa encerre após a geração da senha

escolha = 9

while escolha < 0 or escolha > 4:

    print('Qual Senha estilo de senha deseja gerar?')
    print('Apenas caracteres minusculos = 1')
    print('Apenas numeros = 2')
    print('Caracteres minusculos e numeros = 3')
    print('Caracteres minusculos, maiusculos, numeros e especiais = 4')
    print('Fechar = 0')
    escolha = int(input())
    
if(escolha == 1):
    # senha apenas com caracteres minusculos
    tamanho = int(input('Informe o tamanho da senha: '))
    valores = string.ascii_lowercase
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    print(senha)


if(escolha == 2):
    # senha apenas com numeros
    tamanho = int(input('Informe o tamanho da senha: '))
    valores = string.ascii_lowercase
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    print(senha)

        
if(escolha == 3):
    # senha com caracteres minusculos e numeros
    tamanho = int(input('Informe o tamanho da senha: '))
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)    
    print(senha)

        
if(escolha == 4):
    # senha com caracteres minusculos, maiusculos, numeros e caracteres especiais
    tamanho = int(input('Informe o tamanho da senha: '))
    valores = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)                
    print(senha)            

if(escolha == 0):
    print('Programa Encerrado.')