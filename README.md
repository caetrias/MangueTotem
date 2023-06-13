# mud.e
Código voltado para representação prática do funcionamento do mud.e

AUTORES:

  CIÊNCIA DA COMPUTAÇÃO:

    Alec Carneiro Theotônio

    Ana Lívia da Costa Pessoa

    Gabriel Caetano Galvão Pimentel Farias

    Pedro Wanderley de Lira Santos

  DESIGN:

    Frederico Guedes Klaic

    Julia Silva Brito

    Letícia Souto Maior de Brito

    Lucas Teixeira Catão Ribeiro

 DESCRIÇÃO:

   O nosso projeto "mud.e" se trata de um totem interativo que, de maneira descontraída, apresenta para os usuários informações acerca do ecossitema do mangue e sua preservação bem como 
a atuação do movimento manguebeat para promover a conservação desse ambiente. Essas informações são passadas em formato de vídeos descritivos em conjunto com músicas do manguebeat. Além disso,
o tótem coletará alguns dados dos usuários, os quais deverão responder algumas perguntas durante a apresentação das telas do totem, tais como: idade, gênero, qual a prática de reciclagem mais 
presente no dia a dia do usuário, entre outras. Esses dados servirão para dar uma base estatística acerca do conhecimento sobre o movimento manguebeat e a conservação do ecossistema do manguezal, 
assim como a adesão por parte da população da cidade do Recife à esses temas. Somado a isso, o "mud.e", apresentará uma tela sobre os nossos colaboradores (no momento Instituto Antromangue), 
meios de contato e um QR Code caso o usuário queira contribuir financeiramente com a causa. Por meio desse projeto, acreditamos estar promovendo a preservação ambiental através de tecnologia 
e das ideias do movimento manguebeat.

INSTRUÇÕES DE INSTALAÇÃO:

    Versão da Linguagem: Python 3.11.2
    Configuração de Ambiente:
      Certifique-se de ter essas bibliotecas extras instaladas:
        -> Pygame
        -> Python-vlc
        -> pillow
        -> folium
        -> qrcode
      Pode-se instalar as bibliotecas usando os seguintes no Git Bash
        -> pip install pygame
        -> pip install python-vlc
        -> pip install pillow
        -> pip install folium
        -> pip install qrcode
      Garantir que, ao executar o código e baixar os arquivos necessários, procurar o caminho desse arquivo (vídeo, imagem) no seu dispositivo e substituir no código, tendo em vista que o caminho do arquivo muda de um dispositvo para o
      outro, junto com o método de instalação
     
INSTRUÇÕES DE USO:

    Exemplos de entrada de dados:
      -> IDADE: [1] Menor que 13 anos
                [2] 13 - 16 anos
                [3] 17 - 20 anos
                [4] 21 - 25 anos 
                [5] Maior que 26 anos
                Escolha: 5
     -> GÊNERO: Qual seu Gênero?
                [1] Homem Cis
                [2] Homem Trans
                [3] Mulher Cis
                [4] Mulher Trans
                [5] Outro
                Escolha: 1
     -> RECICLAGEM: QUAL PRÁTICA DE RECICLAGEM VOCÊ CONSIDERA MAIS PRESENTE NO SEU DIA A DIA ? 
                    [1] SEPARAR RESÍDUOS
                    [2] REDUZIR O USO DE MATERIAIS DESCARTÁVEIS
                    [3] COMPRAR PRODUTOS RECICLÁVEIS
                    [4] COMPOSTAGEM
                    Escolha: 3
     -> OPINIÃO SOBRE ATUAÇÃO DO GOVERNO: Diz aí, tu tá gostando do jeito que o governo municipal ta lidando com as questoes ambientais da cidade do Recife?  
                                          [1]Sim, muito!
                                          [2]Acho que pode melhorar!
                                          [3]Não estou gostando.
                                          Escolha: 2


ARQUIVOS:

    Antes de executar o código, certifique-se de ter os seguintes arquivos:

    - CRAB.mp4: Vídeo inicial do totem.
    - Maracatu.mp4: Vídeo informativo.
    - idadegenero.txt: Arquivo para armazenar dados de idade e gênero do usuário.
    - Pergunta 1.txt: Arquivo para armazenar respostas da pergunta 1.
    - Pergunta 2.txt: Arquivo para armazenar respostas da pergunta 2.
    - regioes.txt: Arquivo para armazenar informações sobre a região do usuário.
    - avaliações.txt: Arquivo para armazenar as avaliações dos usuários sobre a experiência no "mud.e"
    -

    Certifique-se de colocar os arquivos nos caminhos corretos conforme foram salvos no seu dispositivo, principalmente os arquivos de imagem/vídeo.
    Você pode encontrá-los na sessão "armazenamento" desse repositório.


PASSOS PARA USAR A APLICAÇÃO:

    1) Faça o clone do repositório do GitHub para o seu repositório local
    2) Abra o seu editor de código-fonte, selecionando o arquivo 'codigo.py'
    1) Certifique-se de ter todas as bibliotecas mencionadas instaladas
    4)Certifique-se de ter os vídeos e outros recursos necessários. Atualize os caminhos de acordo com a localização dos seus arquivos.
    2) Execute o arquivo 'codigo.py'
    3) Siga as instruções fornecidas na interface do terminal. A aplicação apresentará uma série de telas e opções interativas que você pode selecionar com base nas instruções.
    
    OBS.: é imprescindível ter todos os recursos necessários (vídeos, imagens, etc.) nos caminhos específicos do seu dispositivo para que a aplicação funcione de maneira correta.
    




