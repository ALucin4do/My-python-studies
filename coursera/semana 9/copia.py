# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:08:41 2020

@author: Lucino Gabriel
"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    q=0
    s=0
    for w in as_a:
        r=w-as_b[q]
        if r<0:
            r=r*(-1)
        q=q+1
        s=s+r
    
    return s/6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sentenca=separa_sentencas(texto)
    
    for i  in sentenca:
        if i==sentenca[0]:
            frase=separa_frases(i)
        else:
            frase=frase+separa_frases(i)
    
    for k in frase:
        if k==frase[0]:
            palavras=separa_palavras(k)
        else :
            palavras=palavras+separa_palavras(k)
    
    for t in palavras:
        if t==palavras[0]:
            tamanho=len(t)
        else:
            tamanho=tamanho+len(t)
    numero= len(palavras)
    media=tamanho/numero
    
    pdiferentes=n_palavras_diferentes(palavras)
    type_token=pdiferentes/numero
    
    punicas=n_palavras_unicas(palavras)
    hapax=punicas/numero
    
    nsentenca=len(sentenca)
    for j in sentenca:
        if j==sentenca[0]:
            caractsentenca=len(j)
        else:
            caractsentenca=caractsentenca+len(j)
    msentenca=caractsentenca/nsentenca
    
    complexidade=len(frase)/len(sentenca)

    caracterfrase=0
    for g in frase:
        caracterfrase=caracterfrase+len(g)
    tmediofrase=caracterfrase/len(frase)
    return [media,type_token,hapax,msentenca,complexidade,tmediofrase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    n=0
    for t in textos:
        f=calcula_assinatura(t)
        n=n+1
        p=compara_assinatura(f, ass_cp)
        if t!=textos[0]:
            if p<=q:
                r=n
        q=compara_assinatura(f, ass_cp)
    return r

ass=le_assinatura()
tex=le_textos()
n=avalia_textos(tex, ass)
print ("O autor do texto",n,"está infectado com COH-PIAH")