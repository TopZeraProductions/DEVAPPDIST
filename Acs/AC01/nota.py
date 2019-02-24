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

24 - Para os alunos não participantes do PAI, a nota final é considerada como 60% da
média das ACs mais 40% da nota da prova mais os pontos extras;

25 - Para os alunos participantes do PAI, a nota final é considerada como 50% da
média das ACs mais 30% da nota da prova mais 20% da nota do PAI mais os
pontos extras;

26 - Salvar tudo num arquivo chamado “nota.py”.
"""

import sys

sys.tracebacklimit = 0

def validate_freq(frequencia):
    str_errors = ""

    try:
        float(frequencia)
    except:
        str_errors += "Frequencia informada nao foi informada nas devidas especificacoes"
        # raise ValueError("Frequencia informada nao foi informada nas devidas especificacoes")

    if frequencia > 1 or frequencia < 0:
        str_errors += "Frequencia precisa estar entre 0 e 1"
        # raise ValueError("Frequencia precisa estar entre 0 e 1")

    return str_errors

def validate_notas(nota, name):
    if nota > 10 or nota < 0:
        raise ValueError(name + " precisa estar entre 0 e 10")


def aluno_aprovado(freq,
                   acs,
                   prova = 0,
                   sub   = 0,
                   pai   = None,
                   extra = 0):

    err = validate_freq(freq)
    validate_acs(acs)
    validate_notas(prova, "prova")
    validate_notas(sub  , "sub")
    validate_notas(extra, "extra")
    print(err)

    if pai != None:
        validate_notas(pai, "pai")


aluno_aprovado(0, 1, 10, 1, 10, 11)