import subprocess
import folium
import os

def clear():
    os.system('cls')

def TELA_MAPA(): 
    clear()
    mapa = folium.Map(location=[-8.063117141345597, -34.870979364607095])

    folium.Marker([-8.048070371974875, -34.903059432678724],popup= 'Parque das Graças').add_to(mapa)
    folium.Marker([-8.099022465006108, -34.898301002159236],popup= 'Parque dos Manguezais').add_to(mapa)
    folium.Marker([-8.040974088413064, -34.903502369582284],popup= 'Jardim do Baobá').add_to(mapa)

    mapa.save('mapaF.html')

   

    subprocess

    print()
