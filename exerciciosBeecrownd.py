# Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados na operação.

# Entrada
# A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação. 
# A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), 
# indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.


# C = int(input())
# T = input("").upper()
# matriz = []

# for i in range(12):
#     linha = []
#     for j in range(12):
#         linha.append(float(input()))
#     matriz.append(linha)
# resultado = 0.0
# for i in range(12):
#     resultado += matriz[i][C]
# if T == "M":
#     resultado /= 12.0

# print(f"{resultado:.1f}")

# T = input("").upper()
# matriz = []
# for i in range(12):
#     linha = []
#     for j in range(12):
#         linha.append(float(input()))
#     matriz.append(linha)

# resultado = 0.0
# if(i>j and i > 11-j):
#     resultado += matriz[i][j]

# if T == "M":
#     resultado/30.0

# print(f"{resultado:.1f}")

# O = input("").upper()
# matriz = []
# for i in range(12):
#     linha = []
#     for j in range(12):
#         linha.append(float(input()))
#     matriz.append(linha)

# resultado = 0.0
# for i in range(12):
#     for j in range(12):
#         if(j>i and j < 11-i):
#             resultado += matriz[i][j]

# if O == "M":
#     resultado = resultado / 30.0

# print(f"{resultado:.1f}")


while True:
    matriz = []
    n = int(input())
    M = n
    if n == 0:
        break
    for i in range(M):
        linha = []
        for j in range(M):
            linha.append(1+min(i, j,n-i-1, n-j-1))
        matriz.append(linha)
    
    for i in range(M):
        resultado = [str(x).rjust(3) for x in matriz[i]]
        
        print(*resultado, sep=" ")
    print()
    





