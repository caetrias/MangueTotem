""" BIBLIOTECAS EXTRAS INSTALADAS. CASO NÃO AS TENHA, USE COMANDOS NO GIT BASH:
'pip install pygame' 
'pip install python-vlc'
'pip install pillow'
'pip install folium'
"""

import os
import time
import pygame
import datetime
import qrcode
from PIL import Image
import folium
import webbrowser

def abrir_video(caminho):    
    url = "file:///" + caminho.replace("\\", "/")
    webbrowser.open(url)
    #caminho_video = r"CAMINHO\DO\VIDEO" -> CAMINHO PERSONALIZADO PARA CADA USUARIO
    #   abrir_video(caminho_video)


def loading():
    ''' Função para tela de carregamento'''
    clear()
    print("Carregando...")
    time.sleep(1)


def clear():
    '''Função para limpar o terminal'''
    os.system("cls")

def VIDEO_INICIAL (): #C:\Users\LENOVO\Desktop\Projetos\MangueTotem\armazenamento\CRAB
    '''Função para apresentar o vídeo inicial do totem'''

    clear()
    caminho_video = r"C:\Users\LENOVO\Desktop\Projetos\MangueTotem\armazenamento\CRAB.mp4"
    abrir_video(caminho_video)
    time.sleep(3)
    

def tela_inicial():
    '''Função para apresentar a tela inicial do totem e guiar o usuário para a seção desejada'''
    clear()
    VIDEO_INICIAL()
    TELA_REGIAO()
    TELA_PERGUNTA_IDADE()
    TELA_PERGUNTA_GENERO()
    while True:
        try:
            clear()
            print("----[MUD.E]----")
            print("\n\033[1;32;40mJÁ CONHECE O MUD.E?\033[m")
            print("\n[1]SIM")
            print("[2]NÃO")
            decisao = int(input())
            if decisao == 1:
                loading()
                tela_menu()
            if decisao == 2:
                loading()
                TELA_PERGUNTA_1()
                TELA_VIDEO_2()
                TELA_PERGUNTA_2()
                TELA_VIDEO_3()
                TELA_MAPA()
                TELA_COLABORADORES()
                TELA_AGRADECIMENTO()
        except (ValueError,TypeError,EOFError):
            print("Digite um valor inteiro")  #botar cor vermelha

def TELA_PERGUNTA_IDADE():
    clear()
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    try:
        print("\033[1;32;40mQual a sua idade? \033[m")
        print("\n[1] Menor que 13 anos")
        print("[2] 13 - 16 anos")
        print("[3] 17 - 20 anos")
        print("[4] 21 - 25 anos")    
        print("[5] Maior que 26 anos")
        idade = int(input("Escolha: "))
        if idade==1 or idade==2 or idade==3 or idade==4 or idade==5:
            print()
        else:
            clear()
            print("\n\033[1;31;40m---Digite um valor VÁLIDO---\033[m")
            time.sleep(1)
            TELA_PERGUNTA_IDADE()
    except(ValueError,TypeError,EOFError):
        print("\n\033[1;31;40m---Digite um valor INTEIRO---\033[m")
        time.sleep(1)
        TELA_PERGUNTA_IDADE()
            

def TELA_PERGUNTA_GENERO():
    clear()
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    try:
        print("\n\033[1;32;40mQual seu Gênero?\033[m")
        print("\n[1] Homem Cis")
        print("[2] Homem Trans")
        print("[3] Mulher Cis")
        print("[4] Mulher Trans")
        print("[5] Outro")
        sexo = int(input("Escolha: "))
        if sexo == 1:
            f = open("armazenamento/idadegenero.txt", "a",  encoding='utf-8' )
            f.write(f"Gênero: {sexo} | Data e Hora: {data_hora}\n")
            f.close()
        elif sexo == 2:
            f = open("armazenamento/idadegenero.txt", "a",  encoding='utf-8' )
            f.write(f"Gênero: {sexo} | Data e Hora: {data_hora}\n")
            f.close()
        elif sexo == 3:
            f = open("armazenamento/idadegenero.txt", "a",  encoding='utf-8' )
            f.write(f"Gênero: {sexo} | Data e Hora: {data_hora}\n")
            f.close()
        elif sexo == 4:
            f = open("armazenamento/idadegenero.txt", "a",  encoding='utf-8' )
            f.write(f"Gênero: {sexo} | Data e Hora: {data_hora}\n")
            f.close()
        elif sexo == 5:
            f = open("armazenamento/idadegenero.txt", "a",  encoding='utf-8' )
            f.write(f"Gênero: {sexo} | Data e Hora: {data_hora}\n")
            f.close()
    except(ValueError,TypeError,EOFError):
        print("\n\033[1;31;40m---Digite um valor INTEIRO---\033[m")
        time.sleep(1)
        TELA_PERGUNTA_GENERO()



def tela_menu():
    '''Tela que vai apresentar o menu inicial do totem'''
    while True:
        try:
            clear()
            print("----[MUD.E]----")
            print("\n\033[1;32;40mPor onde você gostaria de começar?\033[m") #colorir titulo/diminuir fonte desse print
            print("\n[1]VÍDEO INFORMATIVO")
            print("[2]APOIADORES")
            print("[3]PERGUNTAS")
            print("[4]MAPA")
            decisao = int(input())
            if decisao == 1:
                loading()
                TELA_VIDEO_1()
                TELA_AGRADECIMENTO()
            if decisao == 2:
                loading()
                TELA_COLABORADORES()
                TELA_AGRADECIMENTO()
            if decisao == 3:
                loading()
                TELA_PERGUNTA_1()
                TELA_PERGUNTA_2()
                TELA_AGRADECIMENTO()
            if decisao == 4:
                loading()
                TELA_MAPA()
        except (ValueError,TypeError,EOFError):
             time.sleep(1)
             print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")


def TELA_VIDEO_1():
    '''Função que vai apresentar um dos vídeos para o usuário'''

    caminho_video = r"C:\Users\LENOVO\Desktop\Projetos\MangueTotem\armazenamento\Maracatu.mp4"
    abrir_video(caminho_video)
    time.sleep(3)


def TELA_PERGUNTA_1():
    ''' Função que vai coletar informação do usuário sobre reciclagem'''
    try:
        clear()
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        print('\033[1;32;40mQUAL PRÁTICA DE RECICLAGEM VOCÊ CONSIDERA MAIS PRESENTE NO SEU DIA A DIA ? \033[m')
        print('\n[1] SEPARAR RESÍDUOS')
        print('[2] REDUZIR O USO DE MATERIAIS DESCARTÁVEIS ')
        print('[3] COMPRAR PRODUTOS RECICLÁVEIS ')
        print('[4] COMPOSTAGEM ')
        escolha = int(input('Escolha: '))
        if escolha ==1:                        #tratamento de erro caso numero do input seja diferente dos esperados
            p1 = open("armazenamento/Pergunta 1.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha} | Data e Hora: {data_hora}\n')
            p1.close()
                        
        elif escolha ==2:
            p1 = open("armazenamento/Pergunta 1.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha} | Data e Hora: {data_hora}\n')
            p1.close()
                        
        elif escolha ==3:
            p1 = open("armazenamento/Pergunta 1.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha} | Data e Hora: {data_hora}\n')
            p1.close()
                        
        elif escolha ==4:
            p1 = open("armazenamento/Pergunta 1.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha} | Data e Hora: {data_hora}\n')
            p1.close()

    except(ValueError,TypeError,EOFError):
        print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
        time.sleep(1)
        TELA_PERGUNTA_1()
            

def TELA_VIDEO_2():
    '''Função que vai apresentar o segundo vídeo para o usuário'''

    caminho_video = r"C:\Users\LENOVO\Desktop\Projetos\MangueTotem\armazenamento\Maracatu.mp4"
    abrir_video(caminho_video)
    time.sleep(3)

def TELA_PERGUNTA_2():
    '''Função que vai levantar dados dos usuários sobre a opinião dos mesmos sobre a atuação do governo municipal de Recife nas questões ambientais'''
    try:
        clear()
        print("\033[1;32;40mDiz aí, tu tá gostando do jeito que o governo municipal ta lidando com as questoes ambientais da cidade do Recife?  \033[m")
        print("\n[1]Sim, muito!")
        print("[2]Acho que pode melhorar!")
        print("[3]Não estou gostando.")

        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        escolha2 = int(input('Escolha: '))
        if escolha2 == 1:
            p1 = open("armazenamento/Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha2}| Data e Hora: {data_hora}\n')
            p1.close()
        elif escolha2 == 2:
            p1 = open("armazenamento/Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha2} | Data e Hora: {data_hora}\n')
            p1.close()
        elif escolha2 == 3:
            p1 = open("armazenamento/Pergunta 2.txt", "a",  encoding='utf-8' )
            p1.write(f'{escolha2}| Data e Hora: {data_hora}\n')
            p1.close()
        else: 
            clear()
            print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
            time.sleep(1)
            TELA_PERGUNTA_2()

    except(ValueError,TypeError,EOFError):
        print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
        time.sleep(1)
        TELA_PERGUNTA_2()


def TELA_VIDEO_3():
    '''Função que vai rodar o terceiro vídeo para o usuário'''
    clear()
    caminho_video = r"C:\Users\LENOVO\Desktop\Projetos\MangueTotem\armazenamento\Maracatu.mp4"
    abrir_video(caminho_video)
    time.sleep(3)
    print("[1]Continuar")
    continuar = int(input())
    if continuar ==1:
        print()
    else:
        print("DIGITE UM VALOR VÁLIDO")
        time.sleep(1)
        TELA_VIDEO_3()

def TELA_REGIAO(): # AINDA FALTANDO ADICIONAR AO ARQUIVO
    '''Função que coleta informação sobre a região do usuário, de onde ele vem'''

    clear()
    try:
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        print('\033[1;32;40mVocê é de Recife?\033[m')
        print('[1] Sim')
        print('[2] Não')
        escolha = int(input('Escolha: '))

        if escolha == 1:
            clear()
            
            f = open("armazenamento/regioes.txt", "a", encoding="utf-8")
            f.write(f"Região: Nordeste | Estado: Pernambuco\nData e Hora: {data_hora}\n")
            f.close()

        elif escolha == 2:
            clear()
            regioes = {
                1: "Norte",
                2: "Nordeste",
                3: "Sudeste",
                4: "Sul",
                5: "Centro-Oeste"
            }
            print('\033[1;32;40mDe qual região do Brasil você é?\033[m\n')
        
            for codigo, regiao in regioes.items():
                print(f"[{codigo}] {regiao}")
            regiao_escolhida = int(input('Escolha: '))

            estados = {
                1: ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"],
                2: ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
                3: ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
                4: ["Paraná", "Rio Grande do Sul", "Santa Catarina"],
                5: ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]
            }
            clear()
            for estado_numero, estado in enumerate(estados[regiao_escolhida], start=1):
                print(f"[{estado_numero}] {estado}")

            estado_escolhido_numero = int(input("Qual o seu estado? "))

            estado_escolhido = estados[regiao_escolhida][estado_escolhido_numero - 1]

            time.sleep(2)

            print("Você é da região", regioes[regiao_escolhida], "e do estado", estado_escolhido)

            f = open("armazenamento/regioes.txt", "a", encoding="utf-8")
            f.write(f"Região: {regioes[regiao_escolhida]} | Estado: {estado_escolhido}\nData e Hora: {data_hora}\n")
            f.close()

    except(ValueError,TypeError,EOFError):
        print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
        time.sleep(1)
        TELA_REGIAO()

def TELA_MAPA(): 
    clear()
    mapa = folium.Map(location=[-8.063117141345597, -34.870979364607095])

    folium.Marker([-8.048070371974875, -34.903059432678724],popup= 'Parque das Graças').add_to(mapa)
    folium.Marker([-8.099022465006108, -34.898301002159236],popup= 'Parque dos Manguezais').add_to(mapa)
    folium.Marker([-8.040974088413064, -34.903502369582284],popup= 'Jardim do Baobá').add_to(mapa)

    mapa.save('mapaF.html')

    webbrowser.open('file://' + os.path.abspath('mapaF.html'))

    print('Aí está o mapa com a localização dos totens MUD.E')
    
    time.sleep(3)


def TELA_AGRADECIMENTO():
    '''Apresenta mensagem de agradecimento e pede avaliação.'''
    clear()
    try:
        print("----[OBRIGADO!]----")
        print("\033[1;32;40mO que achou da experiência (0-5)\033[m")
        avalia = int(input('\n'))

        data_hora = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        dados = f"Estrelas: {avalia} | Data e Hora: {data_hora}\n"

        if avalia >=0 and avalia <=5:
            arquivo = open("armazenamento/avaliações.txt", "a")
            arquivo.write(dados)
            print("\n\033[1;36;40mAvaliação armazenada com sucesso!\033[m")
            arquivo.close()
        else:
            print("\n\033[1;31;40mDIGITE UM NÚMERO DE 0 A 5\033[m")
            time.sleep(1.5)
            TELA_AGRADECIMENTO()

    except IOError:
        print("\n\033[1;31;40mErro ao abrir ou escrever no arquivo.\033[m")#ajustar mensagem e ERRO a ser identificado
    except(ValueError,TypeError,EOFError):
        print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
        time.sleep(1)
        TELA_AGRADECIMENTO()


def TELA_COLABORADORES ():
    '''Função que vai exibir as informações dos colaboradores do projeto'''
    try:
        clear()

        # imagem = Image.open("")
        # imagem.show

        print('\n\033[4;37;40mSOBRE:\033[m')

        print('''O Instituto Antromangue promove a manutenção da indentidade social, cultural e ambiental da cidade do Recife, 
        juntamente ao seu desejo de proporcionar uma maior interação entre o público jovem com o movimento Manugebeat.''')

        print()

        print('\n\033[4;37;40mDESEJA AJUDAR?\033[m')

        print('\n\033[4;37;40mCONTATO:\033[m')

        print('antromangue.producoes@gmail.com')

        print()

        qr = qrcode.make('https://nubank.com.br/pagar/p47ub/BVj6iRe45k')
        qr.save('qrcode.jpg')

        imagem2 = Image.open("qrcode.jpg")
        imagem2.show()

        print("[1]Continuar")
        decisao = int(input("Escolha: "))

        if decisao==1:
            loading()
        else:
            print("VALOR INCORRETO")
            time.sleep(1)
            TELA_COLABORADORES()
    except(ValueError,TypeError,EOFError):
        print("\033[1;31;40mValor inserido incorreto, tente novamente...\033[m")
        time.sleep(1)
        TELA_COLABORADORES()

tela_inicial()