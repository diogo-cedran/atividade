# Atividade: Variáveis e Comandos em Programação

# Questão 1: Controle de Fluxo Condicional
# Escreva um programa em Python que peça ao usuário para inserir sua idade. 
# Com base na idade, o programa deve imprimir uma mensagem que indique se a pessoa é uma 
# "criança" (menor de 12 anos), "adolescente" (de 12 a 17 anos), "adulto" (de 18 a 64 anos) 
# ou "idoso" (65 anos ou mais).

# Solicita idade ao usuário
idade = int(input("Digite sua idade: "))

# Determina a categoria da pessoa com base na idade
if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade < 18:
    print("Você é um adolescente.")
elif 18 <= idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

#---------------------------------------------------------------#

# Questão 2: Uso de Loops para Cálculo de Fatorial
# Crie um programa que calcule o fatorial de um número inteiro positivo inserido pelo usuário. 
# O fatorial de um número n é o produto de todos os números inteiros de 1 até n. 
# Use um loop for para implementar a solução.

# Solicita ao usuário um número para calcular o fatorial
numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

# Calcula o fatorial usando loop for
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")

#---------------------------------------------------------------#

# Questão 3: Busca em Lista com Comando de Interrupção
# Escreva um programa que peça ao usuário para inserir um número. 
# O programa deve verificar se esse número está presente em uma lista predefinida de números. 
# Se o número for encontrado, o programa deve imprimir "Número encontrado" e interromper a busca. 
# Caso contrário, deve imprimir "Número não encontrado" ao final da execução.

# Lista predefinida de números
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicita um número ao usuário
numero_busca = int(input("Digite um número para buscar na lista: "))

# Verifica se o número está na lista
numero_encontrado = False
for numero in lista_numeros:
    if numero == numero_busca:
        print("Número encontrado")
        numero_encontrado = True
        break

if not numero_encontrado:
    print("Número não encontrado")
