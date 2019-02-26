# coding=utf-8
"""
1 - O primeiro parâmetro, chamado "freq" é obrigatório e trata-se de um número de
ponto flutuante entre 0 e 1 que indica qual é a proporção de aulas em que o
aluno esteve presente

2 - O segundo parâmetro, chamado "acs" é obrigatório e trata-se de uma lista com
10 elementos que representam as notas das ACs dos alunos

3 - O terceiro parâmetro, chamado "prova", com valor default 0, indica a nota obtida
na prova semestral

4 - O quarto parâmetro, chamado "sub", com valor default 0, indica a nota obtida na
prova substitutiva;

5 - O quinto parâmetro, chamado "pai", com valor default None, indica a nota obtida
no PAI caso o aluno seja participante do PAI ou None em caso contrário;

6 - O sexto parâmetro, chamado "extra", com valor default 0, é um número de ponto
flutuante que indica quantos pontos extras devem ser adicionado à nota final do
aluno;

7 - Todas as notas são representadas por um número de ponto flutuante entre 0 e
10;

8 - ACs e provas que não tiverem sido realizados ou entregues são considerados com
a nota 0;

9 - É considerado inválido o qualquer parâmetro que estiver fora da faixa de valores
esperada, for de um tipo incorreto (especialmente não-numéricos), apresentar-se
mal-formado ou de alguma outra forma em desacordo com as suas respectivas
especificações;

10 - No caso de pelo menos um dos parâmetros revelar-se inválido, uma exceção do
tipo ValueError deverá ser lançada;

11 - No caso de uma exceção ValueError ser lançada, a mensagem de erro deverá
informar o nome do parâmetro cujas restrições foram violadas;

12 - No caso de haver vários parâmetros cujas restrições foram violadas
simultaneamente em uma mesma chamada à função, a mensagem de erro da
exceção pode referir-se a qualquer um desses parâmetros ou mesmo a vários
deles ou até mesmo a todos eles, desde que refira-se a pelo menos um deles;

13 - No caso da exceção ValueError ser lançada, os nomes dos parâmetros que
estavam válidos na chamada da função não devem em hipótese nenhuma
aparecer na mensagem de erro informada;

14 - No caso de todos os parâmetros informados serem válidos, a função deve
retornar um dicionário com dois campos: "aprovado" e "motivo";

15 - O campo "aprovado" deve ser um valor booleano que indica se o aluno foi ou não
aprovado;

16 - O campo "motivo" deve ser uma lista que pode conter as strings "nota" e/ou
"faltas" em qualquer ordem, porém sem repetições, indicando a razão pela qual
o aluno foi reprovado;

17 - Caso o aluno tenha sido aprovado, o campo "motivo" deve conter uma lista vazia;

18 - O aluno com menos do que 75% de frequência é considerado reprovado por
faltas;

19 - O aluno com nota final menor que 6 é considerado reprovado por nota;

20 - Apenas a maior nota dentre a prova semestral e a prova substitutiva será
considerada como nota da prova;

21 - A média das ACs é computada como a média das 7 maiores notas dentre as 10
ACs;

22 - Para os alunos não participantes do PAI, a nota final é considerada como 60% da
média das ACs mais 40% da nota da prova mais os pontos extras;

23 - Para os alunos participantes do PAI, a nota final é considerada como 50% da
média das ACs mais 30% da nota da prova mais 20% da nota do PAI mais os
pontos extras;

24 - Salvar tudo num arquivo chamado “nota.py”.
"""

import sys

sys.tracebacklimit = 0

def validate_freq(frequencia):
    try:
        float(frequencia)
    except:
        return "Frequencia informada nao foi informada nas devidas especificacoes\n"

    if frequencia > 1 or frequencia < 0:
        return "Frequencia precisa estar entre 0 e 1\n"

    return ""


def validate_acs(notas):
    if type(notas) is not list:
        return "Notas enviadas nao foram informadas nas devidas especificacoes\n"

    if len(notas) != 10:
        return "Notas enviadas em numero inferior ao necessitado (10)\n"

    err = ""
    for index , nota in enumerate(notas):
        err += validate_notas(nota, "AC" + str(index + 1))

    return err


def validate_notas(nota, name):
    try:
        float(nota)
    except:
        return "a nota de {0} nao foi informada nas devidas especificacoes\n".format(name)

    if float(nota) > 10 or float(nota) < 0:
        return name + " precisa estar entre 0 e 10\n"

    return ""


def calcular_media_acs(notas):
    media = 0
    for index in range(0, 7):
        media += notas[index] * 1.0

    return media / 7


def aluno_aprovado(freq,
                   acs,
                   prova = 0,
                   sub   = 0,
                   pai   = None,
                   extra = 0):

    dictionary = {}
    dictionary["aprovado"] = True
    dictionary["motivo"]   = []

    err  = ""
    err += validate_freq(freq)
    err += validate_acs(acs)
    err += validate_notas(prova, "prova")
    err += validate_notas(sub  , "sub")
    err += validate_notas(extra, "extra")

    if pai != None:
        err += validate_notas(pai, "pai")

    if len(err) > 0:
        raise ValueError("\n" + err)

    if freq < 0.75:
        dictionary["aprovado"] = False
        dictionary["motivo"].append("Frequencia inferior a 75%")

    if sub > prova:
        prova = sub

    notas.sort(reverse = True)

    media_acs = calcular_media_acs(notas)

    media_final = 0
    if (pai == None):
        media_final = (prova * 0.4) + (media_acs * 0.6) + extra
    else:
        media_final = (prova * 0.3) + (media_acs * 0.5) + (pai * 0.2) + extra

    if (media_final < 6):
        dictionary["aprovado"] = False
        dictionary["motivo"].append("Nota Final Inferior a 6")

    return dictionary

# notas = [7,10,4,7,4,7,7,6,10, 1]
# print(aluno_aprovado(.70, notas, 1, 1, None,1))