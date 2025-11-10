# n, m = map(int, input().split()) 
# matriz = []

# for i in range(n):
#     line = [int (x) for x in input().split()]
#     matriz.append(line)
# print(matriz)

# i = 0
# j = 0
# k = 0
# while k<n:
#     numerosInseridos = list(map(int, input().split()))
#     matriz.append(numerosInseridos)
#     k+=1
#     # print(matriz)

# for i in range (len(matriz[j])):
#         for j in range(len(matriz)):
#             print(matriz[i][j], end="\n")


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

# if len(matriz) > 1:
#     print("não é linha")
# else:
#     print("é matriz linha")


# if m > 1:
#     print("Não é uma matriz coluna")
# else:
#     print("É matriz coluna")

#============================

# n, m = map(int, input().split()) 
# matriz = []

# # for i in range(n):
# #     line = [int (x) for x in input().split()]
# #     matriz.append(line)
# print(matriz)

# if(n == m):
#     ehDiagonal = True
#     for i in range(n):
#         for j in range(m):
#             if(i!=j):
#                 if(matriz[i][j]!=0):
#                     ehDiagonal = False
#     if (ehDiagonal):
#         print("é Diagonal")
#     else:
#         print("não é Diagonal")



# ehNula =True
# for i in range(n):
#     for j in range(m):
#         if(matriz[i][j]!=0):
#             ehNula = False

# if (ehNula):
#     print("é uma matriz nula")
# else:
#     print("não é uma matriz nula")




# n, m = map(int, input().split()) 

# matriz = [[0 for m in range(m)] for n in range(n)]

# # print(matriz)

# for i in range(n):
#     for j in range(m):
#         if(i>j):
#             matriz[i][j] = 10 * i + j
#         elif (j>i) or (j==i):
#             matriz[i][j] = 0
# print(matriz)

n, m = map(int, input().split()) 
matriz = [[0 for m in range(m)] for n in range(n)]

# for i in range(n):
#     line = [int (x) for x in input().split()]
#     matriz.append(line)
print(matriz)



for i in range(n):
    for j in range(m):
        if i == j:
            matriz[i][j] = 1
        elif i+j == n-1:
            matriz[i][j] = -1
        elif i < j:
            matriz[i][j] = 10*i+j
for linha in (matriz):
    print(*linha, sep=" ")