""" BIBLIOTECAS EXTRAS INSTALADAS. CASO NÃO AS TENHA, USE COMANDOS NO GIT BASH:
'pip install pygame'
'pip install python-vlc'

"""

import os
import time
import pygame  
import vlc

def loading():
    clear()
    print("Carregando...")
    time.sleep(1)

def clear():
    os.system("cls")

def tela_inicial():
    clear()
    print("----[Mangue Totem]----")
    print("JÁ CONHECE O MANGUE TOTEM?")
    print("\n[1]SIM")
    print("[2]NÃO")
    decisao = int(input())
    if decisao == 1:
        loading()
        tela_menu()
    if decisao == 2:
        loading()
        PERGUNTA_IDADE()
        VIDEO_MANGUE()


def tela_menu():
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

def VIDEO_MANGUE(): #CODIGO AINDA EM PERIODO DE TESTE - TESTANDO OPÇÕES
    clear()
    # media = vlc.MediaPlayer('Flor de Tangerina.mp4')
    # media.play()

    # while media.is_playing():
    #     continue

    #----------------------------------------------------

    # pygame.init()
    # pygame.mixer.music.load('Flor de Tangerina.mp4')
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     continue
    # pygame.quit()

def PERGUNTA_IDADE():
    clear()
    f = open("informações.txt","a")
    idade= int(input("Qual a sua idade? "))
    genero = input("Qual seu Gênero? ")

    f.write(f"{idade},{genero}")

    f.close()

def TELA_ANIMACAO():
    print()

def TELA_PERGUNTAS():
    print()

def TELA_COLABORADORES():
    print()

def TELA_MAPA():
    print()

tela_inicial()
