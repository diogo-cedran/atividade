# 1) Abstração com Funções e Dicionários

# Implemente uma função chamada calculadora, que utiliza a abstração para realizar diferentes operações matemáticas 
# (adição, subtração, multiplicação e divisão). A função deve receber como parâmetros:
# • Uma string indicando a operação desejada ("adicionar", "subtrair", "multiplicar", "dividir");
# • Dois números para realizar a operação.
# Use um dicionário para mapear strings de operações a funções correspondentes. 
# Caso o usuário passe uma operação inválida, a função deve retornar uma mensagem de erro.

# Definindo funções de operações matemáticas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Divisão por zero não permitida!"
    return x / y

# Definindo a função calculadora
def calculadora(operacao, x, y):
    # Dicionário que mapeia operações a funções
    operacoes = {
        "adicionar": adicionar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir
    }
    
    # Verifica se a operação é válida
    if operacao not in operacoes:
        return "Operação inválida!"
    
    # Retorna o resultado da operação
    return operacoes[operacao](x, y)

# Testando a função calculadora
print(calculadora("adicionar", 10, 5))
print(calculadora("subtrair", 10, 5))
print(calculadora("multiplicar", 10, 5))
print(calculadora("dividir", 10, 5))
print(calculadora("dividir", 10, 0))
print(calculadora("modulo", 10, 5))

#---------------------------------------------------------------#

# 2) Passagem de Parâmetros e Funções de Alta Ordem
# Implemente uma função chamada aplicar_operacao que recebe dois números e uma função como parâmetros. 
# A função fornecida será aplicada aos dois números passados. 
# Crie também uma função chamada gerar_operacao que, com base em uma string de operação ("soma", "multiplicacao"), 
# retorne a função apropriada.

# Função de soma
def soma(a, b):
    return a + b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função que aplica uma operação a dois números
def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

# Função que gera a operação com base na string fornecida
def gerar_operacao(operacao):
    if operacao == "soma":
        return soma
    elif operacao == "multiplicacao":
        return multiplicacao
    else:
        return None

# Testando as funções
op_soma = gerar_operacao("soma")
print(aplicar_operacao(5, 3, op_soma))

op_multiplicacao = gerar_operacao("multiplicacao")
print(aplicar_operacao(5, 3, op_multiplicacao))

#---------------------------------------------------------------#

# 3) Manipulação de Parâmetros Mutáveis e Imutáveis com Funções Aninhadas
# Implemente as seguintes funções:
# • modificar_dicionario: Esta função deve receber um dicionário como parâmetro. 
#   Dentro dela, deve existir uma função aninhada chamada alterar_chave que altera o valor de uma chave específica do dicionário. 
#   A função externa deve chamar a função aninhada para modificar o dicionário;
# • modificar_tupla: Esta função deve receber uma tupla como parâmetro e tentar alterar o valor de um dos elementos da tupla.

# Função para modificar dicionário
def modificar_dicionario(dicionario):
    def alterar_chave(chave, valor):
        if chave in dicionario:
            dicionario[chave] = valor
        else:
            print(f"Chave '{chave}' não encontrada no dicionário.")
    
    # Modificando o dicionário
    alterar_chave("nome", "Novo Nome")
    alterar_chave("idade", 25)

# Testando função modificar_dicionario
meu_dicionario = {"nome": "Antigo Nome", "idade": 20}
modificar_dicionario(meu_dicionario)
print(meu_dicionario)

# Função para modificar tupla
def modificar_tupla(tupla):
    try:
        # Tentativa de modificar um elemento da tupla
        tupla[0] = "Novo Valor"
    except TypeError:
        print("Erro: Tuplas são imutáveis e não podem ser alteradas.")

# Testando função modificar_tupla
minha_tupla = ("Valor Original", 123)
modificar_tupla(minha_tupla)
print(minha_tupla)