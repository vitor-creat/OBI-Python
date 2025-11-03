# matriz = [
#     [1,"l",3],
#     [4,5,"b"],
#     ["rodolfo",2,45 ]
#     ]

# matriz[0].pop(0)

# print(matriz)

# matriz[0].insert(0, 1)

# print(matriz)


# nLC, qSimu = map(int, input().split())

# Matriz = []

# for _ in range(nLC):
#     linha_str = input()
#     Matriz.append([int(letra) for letra in linha_str])
# for _ in range(qSimu):
#     proximo_tabuleiro = [[0 for _ in range (nLC)] for _ in range(nLC)]

#     for Lin in range(nLC):
#         for Col in range(nLC):
#             vizinhos_Vivos = 0
#             for dLin in [-1,0,1]:
#                 for dCol in [-1,0,1]:
#                     if dLin == 0 and dCol == 0:
#                         continue
#                         viz_li, viz_col = Lin + dLin, Col + dCol
#                         if 0 <= viz_li < nLC and 0 <= viz_col < nLC:
#                             vizinhos_Vivos += Matriz[viz_li],[viz_col]
        
#             celula_atual_viva = Matriz[Lin][Col] == 1

#             if vizinhos_Vivos == 3 or (celula_atual_viva and vizinhos_Vivos == 2):
#                 proximo_tabuleiro[Lin][Col] = 1
#     Matriz = proximo_tabuleiro
#     for Lin in range(nLC):
#      print("".join(map(str, Matriz[Lin])))




n, m = map(int, input().split()) 
matriz = []
i = 0
j = 0
k = 0
while k<n:
    numerosInseridos = list(map(int, input().split()))
    matriz.append(numerosInseridos)
    k+=1
    # print(matriz)

for i in range (len(matriz[j])):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\n")


# parte inutil
# while i <= n:
#     linhas = []
#     linhas.append(0)
#     i+=1
#     matriz.append(linhas)
#     while j<=m:
#         colunas = []
#         colunas.append(0)
#         j+=1
#         matriz.append(colunas)


#===========================
#Matriz linha

if len(matriz) > 1:
    print("não é linha")
else:
    print("é matriz linha")


if m > 1:
    print("Não é uma matriz coluna")
else:
    print("É matriz coluna")

#============================
