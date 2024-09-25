# Atividade: Associações e Escopo em Python

# Associações de Variáveis e Escopo Global vs. Local
# • Crie uma função chamada soma() que recebe dois parâmetros a e b e retorna a soma deles;
# • Dentro da função, crie uma variável local resultado que armazena o valor da soma;
# • Fora da função, tente acessar a variável resultado e observe o que acontece;
# • Em seguida, declare uma variável global chamada resultado_global fora da função e, dentro da função,
# modifique seu valor para a soma de a e b.

# Variável global
resultado_global = 0

def soma(a, b):
    # Variável local
    resultado = a + b
    print(f"Resultado dentro da função (local): {resultado}")
    # Modificando a variável global
    global resultado_global
    resultado_global = resultado

# Chamando a função soma
soma(5, 7)

# Tentando acessar a variável local (comentada para evitar erro)
# print(resultado) # Isso vai gerar um erro porque resultado não é acessível fora da função

# Acessando a variável global
print(f"Resultado global: {resultado_global}")

#---------------------------------------------------------------#

# Associações de Variáveis com Funções Aninhadas e nonlocal
# • Crie uma função outer() que contém uma variável contador inicializada em 0;
# • Dentro de outer(), defina uma função incrementar() que incrementa o valor de contador em 1 cada vez que é chamada;
# • Use a palavra-chave nonlocal para permitir que incrementar() modifique o valor de contador dentro de outer();
# • A função outer() deve retornar a função incrementar;
# • Chame a função incrementar() várias vezes e exiba o valor de contador.

def outer():
    contador = 0
    
    def incrementar():
        nonlocal contador
        contador += 1
        print(f"Contador: {contador}")
    
    return incrementar

# Obtendo a função incrementar a partir de outer
incrementar_func = outer()

# Chamando a função incrementar várias vezes
incrementar_func()
incrementar_func()
incrementar_func()

#---------------------------------------------------------------#

# Associações de Variáveis com Condicionais e Escopo
# O que acontece quando você tenta acessar y fora do bloco if?

# Exemplo:
x = 10

if x > 5:
    y = 20


# Se a condição x > 5 for verdadeira, `y` será acessível fora do bloco if.
# Como x é 10, a condição é verdadeira, então `y` é definida.
print(y)  # Isso imprimirá: 20

# Resposta: Se a condição dentro do bloco `if` for verdadeira, a variável `y` será acessível fora do bloco. 
# Caso contrário, se a condição for falsa, a variável `y` não será definida e tentar acessá-la resultará em um erro `NameError`.

#---------------------------------------------------------------#

# Associações de Variáveis com Condicionais e Escopo
# O escopo de uma variável é influenciado pela sua localização dentro de blocos condicionais em Python?

# Exemplo de variável dentro de bloco condicional fora de funções:
x = 10

if x > 5:
    z = 15  # Variável declarada dentro de um bloco if

# A variável `z` é acessível fora do bloco if, pois foi declarada no escopo global
print(z)  # Isso imprimirá: 15

# Se `x` fosse menor ou igual a 5, a variável `z` não seria criada e tentar acessá-la resultaria em erro `NameError`.

# Resposta: Variáveis declaradas em blocos condicionais (fora de funções ou classes) têm escopo global em Python, 
# desde que o bloco seja executado. Se o bloco condicional não for executado, a variável não será criada e tentativas 
# de acesso resultarão em erro.
