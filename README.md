# AppScraping
Con este script en python hacemos scraping a una web.
# Documentacion
- App.py es la aplicacion principal en la que comprobamos el precio de un reloj de la web con el que nosotros estariamos dispuestos a pagar que tenemos almacenado en un fichero de texto.Si esta mas barato nos envia una notificacion a un bot de Telegram creado.
- setPrice.py es el script que modifica el precio maximo a pagar.
- botTelegram.py es el script con la funcion que envia el mensaje al bot de Telegram.
- precioMaximo.txt almacena el precio maximo a pagar.
# Aplicacion
Mediante crontab o con los modulos schedule y time se puede programar para que se ejecute la App de forma periodica, por ejemplo cada dia a una hora concreta.


