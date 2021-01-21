"""Este script consulta el precio actual de un producto de PC Componentes y lo compara con el valor de precio maximo
almacenado en un fichero externo llamado precioMaximo.txt. En caso de que esté mas barato nos enviará un mensaje a 
Telegram a traves de un Bot creado
"""
#Importamos las librerias que necesitamos
import requests
from bs4 import BeautifulSoup
import botTelegram
import os

#url del producto al que deseamos hacer un seguimiento
page = requests.get("https://www.pccomponentes.com/garmin-fenix-5-plus-smartwatch-negro-plata")
soup = BeautifulSoup(page.content, 'html.parser')#Lo parseamos a codigo HTML

#Busca un div cuyo nombre de clase sea precioMain h1
result = soup.find("div",{"class":"precioMain h1"})
#print(result.text)#imprimimos el texto del resultado que NO es codigo html
precioActual_texto = result.text
precioActual = int(precioActual_texto.replace('€',''))#sustituimos la € por un caracte vacio

ficheroPrecio = "precioMaximo.txt"#Poner ruta absoluta

try:
    with open(ficheroPrecio) as f:
        lineas = f.readlines()
        precioDeseado = float(lineas[0])#Guardamos el precio que esta en la primera linea del fichero como float
        
    if precioActual < precioDeseado:
        print("Enhorabuena, hay oferta del producto. Te ahorras: "+str(precioActual - precioDeseado)+" €")
        botTelegram.telegram_bot_sendtext("Enhorabuena, hay oferta del producto. Te ahorras: "+str(precioActual - precioDeseado)+" €")
    else:
        print("Lo sentimos, el producto no esta en oferta")

except FileNotFoundError:
        print(f"No pude encontrar el fichero {ficheroPrecio}")
except:
    print("Error al realizar la operacion")






