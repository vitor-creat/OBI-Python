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

K, N = input("").split(" ")
K = int(K)
N = int(N)


quantidadeChar = input("")
mensagemEnviada = input("")

letrasAlfabeto = list(quantidadeChar)
letrasMensagem = list (mensagemEnviada)

pode = True
for letras in mensagemEnviada:
    if letras not in quantidadeChar:
        pode = False
        break

if pode == True:
    print("S")
else: 
    print("N")

