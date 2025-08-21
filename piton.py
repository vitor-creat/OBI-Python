# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

# Entrada
# A entrada contém um valor inteiro N (5 < N < 2000).

# Saída
# Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

# Tome cuidado! Algumas linguagens tem por padrão apresentarem 576como saída 1e+006 ao 
# invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

# N = int(input())
# QtdNota100 = 0
# QtdNota50 = 0
# QtdNota20 = 0
# QtdNota10 = 0
# QtdNota5 = 0
# QtdNota2 = 0
# QtdNota1 = 0
# if N> 5 and N<1000000:
#     while N >= 100:
#         N -= 100
#         QtdNota100 += 1
#     print(f"{QtdNota100} nota(s) de R$ 100,00")
#     while N >= 50:
#         N -= 50
#         QtdNota50 += 1
#     print(f"{QtdNota50} nota(s) de R$ 50,00")
#     while N >= 20:
#         N -= 20
#         QtdNota20 += 1
#     print(f"{QtdNota20} nota(s) de R$ 20,00")
#     while N >= 10:
#         N -= 10
#         QtdNota10 += 1
#     print(f"{QtdNota10} nota(s) de R$ 10,00")
#     while N >= 5:
#      N -= 5
#      QtdNota5 += 1
#     print(f"{QtdNota5} nota(s) de R$ 5,00")
#     while N >= 2:
#      N -= 2
#      QtdNota2 += 1
#     print(f"{QtdNota2} nota(s) de R$ 2,00")
#     while N >= 1:
#         N -= 1
#         QtdNota1 += 1
#     print(f"{QtdNota1} nota(s) de R$ 1,00")  
        