#CON ESTE SCRIPT GUARDAREMOS EN UN FICHERO EXTERNO EL PRECIO DEL PRODUCTO DESEADO
#SE DEBE EJECUTAR CADA VEZ QUE DESEEMOS CAMBIAR EL PRECIO MAXIMO DEL PRODUCTO
nombreFichero = 'precioMaximo.txt'

try:
    with open(nombreFichero,'w') as f:
        precio = input("Introduzca el precio deseado(Ejemplo:233 ) y pulse intro: ")
        f.write(precio)
        print("Opeacion realizada con exito")
except FileNotFoundError:
    print(f"No se ha podido abrir/modificar el fichero {nombreFichero}")
except:
    print("Error en la operacion con el fichero")

