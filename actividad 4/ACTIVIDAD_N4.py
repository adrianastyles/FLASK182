from tkinter import *
from tkinter import ttk
import tkinter as tk
from controlador_actN4 import *

controlador = controlador()

def Guardar():
    controlador.Guardar(varNombre.get(), varPrecio.get(), varMarca.get(), varTipo.get())
    
def Eliminar():
    msg = messagebox.askquestion("Warning", "¿Está seguro de eliminar la bebida?")
    if (msg == "no"):
        messagebox.showinfo("No eliminado", "Bebida no eliminada")
    else:
        controlador.Eliminar(varID12.get())
        messagebox.showinfo("Eliminado exitoso", "Bebida eliminada")
        
def Consultar():
    bus = controlador.consultarRegistros()
    tabla1.delete(*tabla1.get_children()) #limpia
    for usu in bus:
        tabla1.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3], usu[4]))
    
def ActualizarNom():
    controlador.ActualizarNom(varID3.get(), varNombre1.get())
    
def ActualizarPrecio():
    controlador.ActualizarPre(varID3.get(), varPrecio1.get())
    
def ActualizarMarca():
    controlador.ActualizarMarca(varID3.get(), varMarca1.get())

def ActualizarTipo():
    controlador.ActualizarTipo(varID3.get(), varTipo1.get())
    
def Promedio():
    bus = controlador.promedio()
    for usu in bus:
        cadena1 = str(usu[0])
        textBus.config(state = 'normal')
        textBus.delete(2.0, 'end')
        textBus.insert('end', cadena1)
        textBus.config(state='disabled')
    
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("570x420")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)
pestana6 = ttk.Frame(panel)
pestana7 = ttk.Frame(panel)

#PESTAÑA 1
titulo = Label(pestana1, text = "Registro de bedidas", fg = "blue", font = ("Modern", 18)). pack()
varNombre = tk.StringVar()
varPrecio = tk.StringVar()
varMarca = tk.StringVar()
varTipo = tk.StringVar()

lblNom = Label(pestana1, text = "Nombre:").pack()
txtNom = Entry(pestana1, textvariable = varNombre).pack()

lblPr = Label(pestana1, text = "Precio:").pack()
txtPr = Entry(pestana1, textvariable = varPrecio).pack()

lblMa = Label(pestana1, text = "Marca:").pack()
txtMa = Entry(pestana1, textvariable = varMarca).pack()

lblTi = Label(pestana1, text = "Clasificación:").pack()
txtTi = Entry(pestana1, textvariable = varTipo).pack()

btnGuardar = Button(pestana1, text = "Guardar", command = Guardar).pack()

#PESTAÑA 2
titulo = Label(pestana2, text = "Borrar bebidas", fg = "blue", font = ("Modern", 18)). pack()

varID12 = tk.StringVar()

lblIDD = Label(pestana2, text = "Ingrese el ID:").pack()
txtIDD = Entry(pestana2, textvariable = varID12).pack()
btnB = Button(pestana2, text = "Borrar", command = Eliminar).pack()

#PESTAÑA 3
titulo = Label(pestana3, text = "Actualizar", fg = "blue", font = ("Modern", 18)). pack()

varID3 = tk.StringVar()
varNombre1 = tk.StringVar()
varPrecio1 = tk.StringVar()
varMarca1 = tk.StringVar()
varTipo1 = tk.StringVar()
varCantidad1 = tk.StringVar()

lblID = Label(pestana3, text = "Ingrese el ID:").pack()
txtID = Entry(pestana3, textvariable = varID3).pack()

lblN = Label(pestana3, text = "Nombre:").pack()
txtN = Entry(pestana3, textvariable = varNombre1).pack()
btnN = Button(pestana3, text = "Actualizar nombre", command = ActualizarNom).pack()

lblP = Label(pestana3, text = "Precio:").pack()
txtP = Entry(pestana3, textvariable = varPrecio1).pack()
btnP = Button(pestana3, text = "Actualizar precio", command = ActualizarPrecio).pack()

lblM = Label(pestana3, text = "Marca:").pack()
txtM = Entry(pestana3, textvariable = varMarca1).pack()
btnM = Button(pestana3, text = "Actualizar marca", command =ActualizarMarca).pack()

lblT = Label(pestana3, text = "Clasificación:").pack()
txtT = Entry(pestana3, textvariable = varTipo1).pack()
btnT = Button(pestana3, text = "Actualizar clasificación", command = ActualizarTipo).pack()

#PESTAÑA 4

varBus = tk.StringVar()

titulo = Label(pestana4, text = "Buscar", fg = "blue", font = ("Modern", 18)). pack()
tabla1 = ttk.Treeview (pestana4)
tabla1 ["columns"] = ("Nombre", "Precio", "Marca", "Clasificación")
tabla1.column("#0", width = 60, minwidth = 60)
tabla1.column("Nombre", width = 100, minwidth = 100)
tabla1.column("Precio", width = 200, minwidth = 200)
tabla1.column("Marca", width = 100, minwidth = 100)
tabla1.column("Clasificación", width = 100, minwidth = 100)
tabla1.heading("#0", text = "ID", anchor = tk.CENTER)
tabla1.heading("Nombre", text = "Nombre", anchor = tk.CENTER)
tabla1.heading("Precio", text = "Precio", anchor = tk.CENTER)
tabla1.heading("Marca", text = "Marca", anchor = tk.CENTER)
tabla1.heading("Clasificación", text = "Clasificación", anchor = tk.CENTER)
tabla1.pack()

btnBusqueda = Button(pestana4, text = "Buscar", command = Consultar).pack()

#PESTAÑA 5

varCBM = tk.StringVar()
varCBC = tk.StringVar()

titulo = Label(pestana5, text = "Calcular precio promedio", fg = "blue", font = ("Modern", 12)). pack()
textBus = tk.Text(pestana5, height=2, width=20)
textBus.pack()
btnT = Button(pestana5, text = "Calcular", command = Promedio).pack()
titulo1 = Label(pestana5, text = "Cantidad de bebidas de una marca", fg = "blue", font = ("Modern", 12)). pack()
lblCBM = Label(pestana5, text = "Marca:").pack()
txtCBM = Entry(pestana5, textvariable = varCBM).pack()
lblR = Label(pestana5, text = "Resultado:").pack()
textBus2 = tk.Text(pestana5, height=2, width=20)
textBus2.pack()
btnT2 = Button(pestana5, text = "Buscar").pack()
titulo2 = Label(pestana5, text = "Cantidad por clasificación", fg = "blue", font = ("Modern", 12)). pack()
lblCBC = Label(pestana5, text = "Clasificación:").pack()
txtCBC = Entry(pestana5, textvariable = varCBC).pack()
lblR = Label(pestana5, text = "Resultado:").pack()
textBus3 = tk.Text(pestana5, height=2, width=20)
textBus3.pack()
btnT2 = Button(pestana5, text = "Buscar").pack()


panel.add(pestana1, text = 'Alta')
panel.add(pestana2, text = 'Baja')
panel.add(pestana3, text = 'Actualizar')
panel.add(pestana4, text = 'Mostrar todas')
panel.add(pestana5, text = 'Cálculos')


Ventana.mainloop()