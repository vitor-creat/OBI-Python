# Luiza está se preparando para começar a estudar em uma nova escola que será inaugurada na
# avenida em que ela mora. A avenida possui 2,000 metros de comprimento e existe um ponto de
# ônibus a cada 400 metros, incluindo no início e no fim da avenida. A tabela abaixo indica a distância
# de cada ponto de ônibus para o início da avenida.
# Ponto 
# #1 Ponto 
# 0m
# #2 Ponto
# 400 m 
# #3 Ponto 
# 800 m
# #4 Ponto 
# 1200 m
# #5 Ponto 
# 1600 m
# #6
# 2000 m
# A casa de Luiza está localizada no início da avenida, junto ao primeiro ponto de ônibus. A escola,
# por outro lado, está localizada a uma distância D do início da avenida.
# Luiza pretende pegar o ônibus na porta de casa, descer no ponto de ônibus mais próximo da escola
# e andar a pé o restante do trajeto. Assim, por exemplo, se a escola está a uma distância D = 720 m
# do início da avenida, ela vai descer no terceiro ponto de ônibus, localizado a 800 metros do início,
# e andar 80 metros (em direção ao início da avenida) para chegar à escola.
# Luiza pediu sua ajuda para descobrir quantos metros ela precisará andar: dada a distância em
# metros D da escola para o início da avenida, determine qual a distância entre a escola e o ponto de
# ônibus mais próximo.

# D = int(input())

# if D <= 199:
#     print(0 - D)
# elif D <= 599:
#     print(400 - D)
# elif D <= 999:
#     print(800 - D)
# elif D <= 1399:
#     print(1200-D)
# elif D <= 1799:
#     print(1600 - D)
# else:
#     print(2000 - D)

# Entrada
# A primeira linha de entrada contém dois inteiros K e N separados por um espaço em branco,
# indicando, respectivamente, o número de caracteres presentes no alfabeto alienígena e o número de
# caracteres da mensagem enviada.
# A segunda linha de entrada contém K caracteres distintos representando os caracteres pertencentes
# ao alfabeto alienígena.
# A terceira linha de entrada contém N caracteres (não necessariamente distintos) representando a
# mensagem enviada.
# Saída
# Seu programa deverá imprimir uma única linha contendo um único caractere: se a mensagem pode
# ter sido escrita no alfabeto alienígena, imprima a letra ‘S’ maiúscula; caso contrário, imprima a
# letra ‘N’ maiúscula.

# K, N = input("").split(" ")
# K = int(K)
# N = int(N)


# quantidadeChar = input("")
# mensagemEnviada = input("")

# letrasAlfabeto = list(quantidadeChar)
# letrasMensagem = list (mensagemEnviada)

# pode = True
# for letras in mensagemEnviada:
#     if letras not in quantidadeChar:
#         pode = False
#         break

# if pode == True:
#     print("S")
# else: 
#     print("N")


# Sua tarefa é: dadas as dimensões N e M da pista de dança, a quantidade P de passos da dança e
# a ordem dada pelo professor a cada passo, determine qual aluno estará em cada quadrado da pista
# ao fim da dança.
# Entrada
# A primeira linha da entrada é composta por três inteiros N, M e P indicando, respectivamente, o
# número de linhas da pista de dança, o número de colunas da pista de dança, e o número de passos
# da dança.
# As próximas P linhas descrevem as ordens dadas pelo professor. A i-ésima dessas linhas contém
# uma letra maiúscula Oi
# , que pode ser ‘L’ ou ‘C’, seguida de dois inteiros distintos Ai e Bi
# .
# • Se Oi = ‘L’, o professor ordenou a troca das linhas Ai e Bi
# .
# • Se Oi = ‘C’, o professor ordenou a troca das colunas Ai e Bi
# .


# # N,M,
# P = 3 #input("").split()
# N = 4 #int(N)
# M = 3 #int(M)
# P = int(P)

# #inline
# Matriz = []
# for i in range(N):
#     Matriz.append([int(M*i+x+1) for x in range(M)])
# # print(Matriz)

#cria uma varivel que começa no 1
# cres = 1
# #cria um for que percore de i até N
# #dentro tem um j que vai ate M
# #dentro desse segundo for pega as posições i e j da matriz e atribui o valor da variavel cres para cada um
# #depois acrescenta +1 em cada posição
# for i in range(N):
#     for j in range(M):
#         Matriz[i][j] = cres
#         cres = cres + 1
#print(Matriz)
# i = 0
# auxiliar = 0
# while (i < P):
#     comandoDanca,linha,coluna = input("De um comando L ou C seguido das linhas e colunas: ").split()
#     linha = int(linha)
#     coluna = int(coluna)
#     i+= 1
#     if comandoDanca == "C":
#      for i in range(coluna):


N, Q = map(int, input().split())
D = list(map(int, input().split()))

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    soma = sum(D[l:r+1])
    tam = r - l + 1
    resp = (tam - 1) * soma * 11 
    print(resp)
