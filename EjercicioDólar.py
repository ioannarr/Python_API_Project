#Ejercicio Dólar: //https://www.dolarsi.com/api/api.php?type=valoresprincipales

import requests
import tkinter as tk
from tkinter import *
from tkinter import font


def traer():
    try:
        r = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
        datos = r.json()
        print(datos)
        dolart = datos[0]["casa"]["venta"]
        print(dolart)
        valor1.insert(0,dolart)
        dolart = dolart.replace(",",".")
        print(dolart)
        dolar1 = float(dolart)
        print(dolar1)
        print(f'Dolar Oficial a la Venta: $ {dolar1}')
        
        dolarv = datos[0]["casa"]["compra"]
        print(dolarv)
        valor2.insert(0,dolarv)
        dolarv = dolarv.replace(",",".")
        print(dolarv)
        dolar2 = float(dolarv)
        print(dolar2)
        print(f'Dolar Oficial a la Compra: $ {dolar2}')
    except:
       print("Error en la Api. ")
    
    return dolart

#traer()

ventana = tk.Tk()
ventana.title("Cotizacion del dolar en Argentina usando API")
ventana.geometry("600x300")
ventana.config(bg="lightgrey")

myfont = font.Font( family = "Verdana", size = 15, weight = "bold")

boton = tk.Button(ventana, text='Consultar', command=traer)
boton.grid(row=4, column=2, columnspan=4 )

label1 =tk.Label(ventana, text='Cotizacion a la Compra: ', font=myfont)
label1.grid( row= 1, sticky=tk.W, padx=5, pady=5, ipadx=5, ipady=5)

valor1 = tk.Entry(ventana, width= 30)
valor1.grid(row=1, column= 3, sticky=tk.E, padx=5, pady=5, ipadx=5, ipady=5)

label1 =tk.Label(ventana, text='Cotizacion a la Venta: ', font=myfont)
label1.grid( row= 3, sticky=tk.W, padx=5, pady=5, ipadx=5, ipady=5)

valor2 = tk.Entry(ventana, width= 30)
valor2.grid(row=3, column= 3, sticky=tk.E, padx=5, pady=5, ipadx=5, ipady=5)






ventana.mainloop()
