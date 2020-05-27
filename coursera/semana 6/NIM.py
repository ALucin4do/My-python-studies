# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:56:17 2019

@author: Lucino Gabriel
"""
def computador_escolhe_jogada(N,M):
    j=0
    multiplo=False
    while j<N:
        if j%(M+1)==0:
            r=j
            multiplo=True
        j=j+1
    if multiplo==True and (N-r)<=M:
        t=N-r
    else:
        t=M
    print("O computador tirou",t,"peças.")
    return t


def usuario_escolhe_jogada(N,M):
   
    valido=False
    while valido==False:
        h=int(input("Quantas peças você vai tirar?"))  
        if h>0 and h<=M:
            valido=True
            t=h
        else:
            valido=False
            print("Oops! Jogada inválida! Tente de novo.",)
    return t

                
def partida():
    N=int(input("Quantas peças?"))
    M=int(input("Limite de peças por jogada?"))
    f=0
    é_multiplo=0
    while f<=100:
        f=f+1
        if N==f*(M+1):
            é_multiplo=é_multiplo+1
    if é_multiplo== 0:
        print("Computador começa!")
        C=0 
        U=1
        while N>0:
            if C==0 and U==1:
                y=computador_escolhe_jogada(N,M)
                N=N-y
                C=1
                U=0
                print("Agora restam apenas",N,"peças no tabuleiro")
            else:
                z=usuario_escolhe_jogada(N,M)
                N=N-z
                C=0
                U=1
                print("Agora restam apenas",N,"peças no tabuleiro")
        print("Fim do jogo! O computador ganhou!")
    else:
         print("Voce começa!")
         C=1 
         U=0
         while N>0:
            if C==1 and U==0:
                z=usuario_escolhe_jogada(N,M)
                N=N-z
                C=0
                U=1
                print("Agora restam apenas",N,"peças no tabuleiro")
               
            else:
                y=computador_escolhe_jogada(N,M)
                N=N-y
                C=1
                U=0
                print("Agora restam apenas",N,"peças no tabuleiro")
                
         print("Fim do jogo! O computador ganhou!")
    return ()


def campeonato():
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print ("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")
    return ()

x=1
while x!=0:
    print("")
    print("")
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("0 - sair do jogo :(")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    x=int(input())

    if x==1:
        print("Voce escolheu uma Partida!")
    
        partida()
    else:
        if x==2:
          print("Voce escolheu um Campeonato!")
          campeonato()
        else:
            print ("numero inválido")
      


