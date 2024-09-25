# Atividade: Valores, Tipos e Variáveis

# 01) Manipulando variáveis faça:
# 1. Crie variáveis para nome, preço e quantidade em estoque;
# 2. Calcule o valor total do estoque;
# 3. Imprima as informações.

# Criando variáveis
nome_produto = "Camiseta"
preco_produto = 29.99
quantidade_estoque = 100

# Calculando o valor total do estoque
valor_total_estoque = preco_produto * quantidade_estoque

# Imprimindo as informações
print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto:.2f}")
print(f"Quantidade em estoque: {quantidade_estoque}")
print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")

#---------------------------------------------------------------#

# 02) Utilizando conversão Explícita faça:
# 1. Converta a string para inteiro;
# 2. Converta o inteiro para float;
# 3. Converta o float para string;
# 4. Imprima os resultados e seus tipos.

# Criando uma variável string para conversão
valor_string = "42"

# Convertendo a string para inteiro
valor_inteiro = int(valor_string)
print(f"Valor inteiro: {valor_inteiro}, Tipo: {type(valor_inteiro)}")

# Convertendo o inteiro para float
valor_float = float(valor_inteiro)
print(f"Valor float: {valor_float}, Tipo: {type(valor_float)}")

# Convertendo o float para string
valor_string_novamente = str(valor_float)
print(f"Valor string: {valor_string_novamente}, Tipo: {type(valor_string_novamente)}")

#---------------------------------------------------------------#


# 03) Entender escopo de variáveis:
# Crie um trecho de código onde ao menos tenha 2 escopos de código um Global e outro Local.
# Identifique com comentário os escopos das variáveis.

# Variável global
mensagem_global = "Olá, eu sou uma variável global!"

def funcao_exemplo():
    # Variável local
    mensagem_local = "Olá, eu sou uma variável local!"
    print(mensagem_local)

# Acessando variáveis dentro e fora da função
funcao_exemplo()
print(mensagem_global)
# print(mensagem_local) # Descomente esta linha para ver que variável local não é acessível fora da função

#---------------------------------------------------------------#

# 04) Alocação de Memória
# Crie um trecho de código onde:
# 1. Instanciação de 3 variáveis com valor;
# 2. Apresente os endereçamentos de memória alocados;
# 3. Limpe os valores das variáveis;
# 4. Apresente o endereçamento de memória.

# Instanciação de variáveis
a = 10
b = 20
c = 30

# Apresentando endereçamentos de memória
print(f"Endereço de memória de a: {id(a)}")
print(f"Endereço de memória de b: {id(b)}")
print(f"Endereço de memória de c: {id(c)}")

# Limpando valores das variáveis
a = b = c = None

# Apresentando endereçamentos de memória após limpeza
print(f"Endereço de memória de a: {id(a)}")
print(f"Endereço de memória de b: {id(b)}")
print(f"Endereço de memória de c: {id(c)}")
