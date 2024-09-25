# Atividade: Variáveis Tuplas e Dicionários, Classes em Programação

# Atividade 1: Manipulação de Tuplas
# Uma loja de eletrônicos quer armazenar informações sobre seus produtos em tuplas. 
# Cada tupla contém três elementos: o nome do produto, o preço e a quantidade em estoque.
# Escreva um programa em Python que:
# Crie uma tupla para três produtos diferentes.
# Exiba o nome do produto mais caro.
# Calcule o valor total em estoque (preço * quantidade) para cada produto e exiba o resultado.

# Criando tuplas para os produtos
produto1 = ("Celular", 1500.00, 10)
produto2 = ("Notebook", 3500.00, 5)
produto3 = ("Tablet", 1000.00, 8)

# Armazenando os produtos em uma lista de tuplas
produtos = [produto1, produto2, produto3]

# Determinando o produto mais caro
produto_mais_caro = max(produtos, key=lambda produto: produto[1])
print(f"O produto mais caro é: {produto_mais_caro[0]}")

# Calculando o valor total em estoque para cada produto
for produto in produtos:
    valor_total_produto = produto[1] * produto[2]
    print(f"Produto: {produto[0]}, Valor total em estoque: R$ {valor_total_produto:.2f}")

#---------------------------------------------------------------#

# Atividade 2: Uso de Dicionários para Armazenar e Consultar Informações
# Você é encarregado de criar um sistema simples de gerenciamento de informações de alunos usando dicionários.
# O sistema deve:
# Armazenar o nome de três alunos e suas notas em um dicionário, onde o nome é a chave e a nota é o valor.
# Permitir que o usuário insira o nome de um aluno para consultar a nota.
# Exibir a média das notas dos alunos armazenados.

# Criando dicionário com alunos e suas notas
alunos = {
    "João": 8.5,
    "Maria": 7.2,
    "Pedro": 9.0
}

# Consulta de nota
nome_aluno = input("Digite o nome do aluno para consultar a nota: ")
if nome_aluno in alunos:
    print(f"Nota do {nome_aluno}: {alunos[nome_aluno]}")
else:
    print("Aluno não encontrado!")

# Calculando a média das notas
media_notas = sum(alunos.values()) / len(alunos)
print(f"Média das notas dos alunos: {media_notas:.2f}")

#---------------------------------------------------------------#

# Atividade 3: Criando uma Classe para Gerenciar Alunos
# Você deve criar um sistema de gerenciamento de alunos utilizando uma classe em Python. A classe Aluno deve armazenar informações
# sobre o nome do aluno, a idade e as notas em três disciplinas. Além disso, a classe deve ter métodos para:
# Calcular a média das notas.
# Determinar se o aluno foi aprovado ou reprovado (considerando média 7.0 como aprovação).
# Exibir um resumo com o nome, idade, média e status de aprovação do aluno.

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        return self.calcular_media() >= 7.0

    def exibir_resumo(self):
        media = self.calcular_media()
        status = "Aprovado" if self.verificar_aprovacao() else "Reprovado"
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")

# Criando um objeto da classe Aluno
aluno1 = Aluno("Ana", 16, [7.5, 8.0, 9.0])
aluno1.exibir_resumo()

