import os
import time

def loading():
    clear()
    print("Carregando...")
    time.sleep(1)

def clear():
    os.system("cls")

def tela_inicial():
    clear()
    print("----[Mangue Totem]----")
    print("\nPor onde você gostaria de começar?") #colorir titulo/diminuir fonte desse print
    print("\n[1]ANIMAÇÃO")
    print("[2]PERGUNTAS")
    print("[3]COLABORADORES")
    print("[4]MAPA")
    decisao = int(input())
    if decisao == 1:
        loading()
        TELA_ANIMACAO()
    if decisao == 2:
        loading()
        TELA_PERGUNTAS()
    if decisao == 3:
        loading()
        TELA_COLABORADORES()
    if decisao == 4:
        loading()
        TELA_MAPA()

def PERGUNTA_IDADE():
    clear()
    idade= int(input("Qual a sua idade?"))
    genero = input()

def TELA_ANIMACAO():
    print()

def TELA_PERGUNTAS():
    print()

def TELA_COLABORADORES():
    print()

def TELA_MAPA():
    print()

tela_inicial()
