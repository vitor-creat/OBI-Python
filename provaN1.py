# Cláudia trabalha na OBI (Organização dos Bons Informáticos), que recentemente realizou um concurso para contratar novos funcionários.
#  Agora, Cláudia tem a tarefa de determinar a nota de
# corte para o concurso. Chamamos de nota de corte a nota mínima necessária para ser aprovado no
# concurso. Ou seja, se a nota de corte do concurso for C, então todos os participantes com uma nota
# maior ou igual a C serão aprovados no concurso e todos com nota menor que C serão reprovados.
# Seu chefe pediu para que Cláudia aprove no mínimo K candidatos do concurso para a próxima fase,
# mas ela também não quer que a nota de corte seja muito baixa. Por isso, Cláudia decidiu que a
# nota de corte deverá ser a maior nota C que faz com que no mínimo K candidatos sejam aprovados.
# Sua tarefa é: dados o número N de candidatos, as notas A1, A2, ..., AN dos candidatos e a quantidade
# mínima de aprovados K, diga qual deve ser a maior nota de corte C para que pelo menos K
# candidatos sejam aprovados.
# Entrada
# A primeira linha da entrada contém dois inteiros, N e K, representando, respectivamente, o número
# de participantes e o número mínimo de candidatos que devem ser aprovados.
# A segunda linha da entrada contém N inteiros Ai, representando as notas dos participantes.
# Saída
# Seu programa deve imprimir uma linha contendo um único inteiro C, a nota de corte que deve ser
# escolhida por Cláudia.

# N, K = input("").split(" ")
# N = int(N)
# K = int(K)
# notas = input("")
# notas = [int (i) for i in notas.split()]
# notas.sort(reverse=True)
# C = K - 1
# print(notas[C])



# A Seleção de Basquete Campinense (SBC) está ansiosa para disputar a final do campeonato nacional
# universitário contra o Clube de Basquete Sergipano (CBS), o arquirrival da SBC. Entretanto, a
# comissão organizadora esteve sobrecarregada e acabou cometendo alguns erros logísticos, o que
# levou o jogo a ser adiado em exatamente T segundos. A comissão já está trabalhando dobrado e
# precisa da sua ajuda para reajustar o horário do jogo.
# A sua tarefa é: dado o horário original de início do jogo e o tempo T, em segundos, em que o jogo
# foi adiado, determine o novo horário de início do jogo.
# Entrada
# A entrada contém quatro linhas. As três primeiras linhas indicam o horário original de início do
# jogo: a primeira linha contém um inteiro H, que indica as horas. A segunda linha contém um
# inteiro M, que indica os minutos. A terceira linha contém um inteiro e S, que indica os segundos.
# A quarta linha contém um único inteiro T, indicando em quantos segundos o jogo foi adiado.
# Note que o horário é dado no formato de 24 horas, ou seja, H é um inteiro entre 0 e 23.
# Saída
# Seu programa deve imprimir o novo horário de início do jogo, seguindo o mesmo formato de horário
# da entrada. Ou seja, seu programa deve imprimir três linhas, cada uma contendo um único inteiro:
# • A primeira linha deve conter as horas do novo horário de início do jogo.
# • A segunda linha deve conter os minutos do novo horário de início do jogo
# • A terceira linha deve conter os segundos do novo horário de início do jogo.
# Observe que você não deve imprimir zeros à esquerda (veja o exemplo de saída 2).

# #Horario inicial original
# Horas 
H = int(input())
# Minutos
M = int(input())
# Segundos
S = int(input())

# #Tempo em que foi adiado em segundos
T = int(input())

S = S+T
if S>=60:
    M = M+(S//60)
    S=S%60
if M>=60:
    H = H+(M//60)



# Ogro e Bicho-Papão têm fama de malvados, mas na verdade são amáveis, honestos e trabalhadores,
# além de vizinhos e amigos. O Bicho-Papão tem dificuldades em aprender aritmética e por isso
# o Ogro inventou uma brincadeira simples para auxiliar seu amigo: o Ogro inicia mostrando um
# certo número de dedos na sua mão esquerda (vamos chamar esse valor de E) e um número de dedos
# diferente na mão direita (vamos chamar esse valor de D). Então, Bicho-Papão deve falar o resultado
# da brincadeira, definido assim:

# • se o número de dedos na mão esquerda é maior do que o número de dedos na mão direita (ou
# seja E > D) então o resultado é a soma dos dois números (ou seja E + D);
# • caso contrário, o resultado é o dobro da diferença entre o número de dedos na mão direita e
# o número de dedos na mão esquerda (ou seja, 2 × (D − E)).

# O problema é que o Ogro também não é lá muito bom em aritmética, e pediu sua ajuda para
# conferir se o Bicho-Papão falou a resposta correta.
# Dados o número de dedos mostrados na mão esquerda (E) e o número de dedos mostrados na mão
# direita (D), escreva um programa para determinar a resposta da brincadeira.
# Entrada
# A entrada é composta por duas linhas. A primeira linha contém um inteiro E, o número de dedos
# mostrados na mão esquerda. A segunda linha contém um inteiro D, o número de dedos mostrados
# na mão direita.
# Saída
# Seu programa deve produzir uma única linha na saída, contendo um único número inteiro, o resultado da brincadeira.



# E = int(input())
# D = int(input())

# if E>D:
#     print(f"{E+D}")
# else:
#     print(f"{2*(D-E)}")
    