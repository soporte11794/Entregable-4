import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
data = {}
data['pokemon'] = []
rows = ['Nombre','Peso','Tamaño','Tipos','Movimientos']

pokemon = input('Coloca el nombre de un Pokemon: ')

url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
respuesta = requests.get(url)

if respuesta.status_code != 200:
    print('Pokemon no encontrado')
    exit()
    
datos = respuesta.json()
try:
    url_image = datos ['sprites']['front_default']
    imagen = Image.open(urlopen(url_image))
except:
    print('El pokemon no tiene imagen')
    exit()
nombre = datos ['name']
peso = datos ['weight']
tamaño = datos ['height']
movimientos = datos ['moves']
tipos = datos ['types']
lista = ""
lista_tipos = ""
for i in range (int(len(tipos))):
    tipo  = tipos[i]['type']['name']
    if i==0:
        lista_tipos = tipo
    else:
        lista_tipos = lista_tipos + ' , '+ tipo
for j in range (int(len(movimientos))):
    movimiento  = movimientos[j]['move']['name']
    if j==0:
        lista = movimiento
    else:
        lista = lista + ' , '+ movimiento

cell_text = [[nombre],[peso],[tamaño],[lista_tipos],[lista]]
plt.axis('off')

the_table = plt.table(
    cellText= cell_text,
    cellLoc='left',
    rowLabels=rows,
    loc='bottom')
the_table.auto_set_font_size(False)
the_table.set_fontsize(9)
imgplot = plt.imshow(imagen)
plt.subplots_adjust(left=0.2, bottom=0.2)
print('Los movimientos que puede aprender ',nombre,' son: ', lista)

data['pokemon'].append({
    'Nombre': nombre,
    'Peso': peso,
    'Tamano': tamaño,
    'Tipo': lista_tipos,
    'Movimientos': lista})
with open('pokedex.json', 'w') as file:
    json.dump(data, file, indent=4)
plt.show()





