""" BIBLIOTECAS EXTRAS INSTALADAS. CASO NÃO AS TENHA, USE COMANDOS NO GIT BASH:
'pip install pygame'
'pip install python-vlc'
'pip install opencv-python'
"""

import os
import time
import pygame
#import vlc
#import cv2
import datetime


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
        TELA_PERGUNTA_IDADE()
        TELA_PERGUNTA_1()
        TELA_PERGUNTA_2()
        VIDEO_MANGUE()
        TELA_AGRADECIMENTO()


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
        TELA_PERGUNTA_1()
        TELA_PERGUNTA_2()
        TELA_AGRADECIMENTO()
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

def TELA_PERGUNTA_IDADE():
    clear()
    f = open("idadegenero.txt","a",  encoding='utf-8')
    idade= int(input("Qual a sua idade? "))
    genero = input("Qual seu Gênero? ")

    f.write(f"Idade:{idade} | Gênero:{genero}\n")

    f.close()

def TELA_ANIMACAO():
    # video1 = cv2.VideoCapture('Flor de tangerina.mp4')

    # while True:
    #     ret,frame = video.read()
    #     if not ret:
    #         break
    #     cv2.imshow('Video',frame)
    #     if cv2.waitKey(1) & 0xFF == ord('S'):
    #         break
    # video.realese()
    # cv2.destroyAllWindows()
    print()

def TELA_PERGUNTA_1():
    clear()

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

    print('Você costuma fazer reciclagem ? ')
    print('\n[1] Sim, sempre!')
    print('[2] Às vezes! ')
    print('[3] Não, nunca pensei sobre... ')
    print('[4] Não, pretendo começar a fazer assim que souber mais a respeito! ')
    escolha = int(input('Escolha: '))
    if escolha ==1:
        p1 = open("Pergunta 1.txt", "a",  encoding='utf-8' )
        p1.write(f'Sim, sempre! | Data e Hora: {data_hora}\n')
        p1.close()
    elif escolha ==2:
        p1 = open("Pergunta 1.txt", "a",  encoding='utf-8' )
        p1.write(f'Às vezes! | Data e Hora: {data_hora}\n')
        p1.close()
    elif escolha ==3:
        p1 = open("Pergunta 1.txt", "a",  encoding='utf-8' )
        p1.write(f'Não, nunca pensei sobre... | Data e Hora: {data_hora}\n')
        p1.close()
    elif escolha ==4:
        p1 = open("Pergunta 1.txt", "a",  encoding='utf-8' )
        p1.write(f'Não, pretendo começar a fazer assim que souber mais a respeito! | Data e Hora: {data_hora}\n')
        p1.close()

def TELA_PERGUNTA_2():
    try:
        clear()
        print("Diz aí, tu tá gostando do jeito que o governo municipal ta lidando com as questoes ambientais da cidade do Recife?  ")
        print("[1]Sim, muito!")
        print("[2]Acho que pode melhorar!")
        print("[3]Não estou gostando.")

        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        escolha = int(input())
        if escolha ==1:
            p1 = open("Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'Sim, muito! | Data e Hora: {data_hora}\n')
            p1.close()
        elif escolha ==2:
            p1 = open("Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'Acho que pode melhorar! | Data e Hora: {data_hora}\n')
            p1.close()
        elif escolha ==3:
            p1 = open("Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'Não estou gostando. | Data e Hora: {data_hora}\n')
            p1.close()

    except(ValueError):
        print("Valor inserido incorreto, tente novamente...")
        time.sleep(1)
        TELA_PERGUNTA_2()


def TELA_COLABORADORES(): # ONGS/SITE
    clear()
    print()

def TELA_MAPA(): 
    clear()
    print()

def TELA_AGRADECIMENTO():
    clear()
    try:
        print("----[OBRIGADO!]----")
        print("O que achou da experiência (0-5)")
        avalia = int(input())

        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        dados = f"Estrelas: {avalia} | Data e Hora: {data_hora}\n"

        if avalia >=0 and avalia <=5:
            arquivo = open("avaliações.txt", "a")
            arquivo.write(dados)
            print("Avaliação armazenada com sucesso!")
            arquivo.close()
        else:
            print("DIGITE UM NÚMERO DE 0 A 5")
            time.sleep(1.5)
            TELA_AGRADECIMENTO()

    except IOError:
        print("Erro ao abrir ou escrever no arquivo.") #ajustar mensagem e ERRO a ser identificado


tela_inicial()
