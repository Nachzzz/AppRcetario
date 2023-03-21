import json
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog



class AppReceta:
    def __init__(self, master):
        self.master = master
        master.title("App Recetas")

        # Crear widgets para la lista de recetas
        
        self.listaRecetas = tk.Listbox(root)
        self.listaRecetas.pack(side= "right", padx=50, pady=0)
        self.listaRecetas.configure(height=10, width=50)
        
        

        # Crear widgets para los botones
        

        frame = tk.Frame(master)
        frame.pack(side="left", padx="52", pady="50")
        frame.configure(background="#7BC0B8")

        
        self.imgBtn = PhotoImage(file="img0.png")
        self.imgBtn1 = PhotoImage(file="img1.png")
        self.imgBtn2 = PhotoImage(file="img2.png")
        self.imgBtn3 = PhotoImage(file="img3.png")

        self.boton_agregar = tk.Button(frame, text="Agregar Receta", command=self.agregarReceta, image=self.imgBtn, borderwidth=0)
        self.boton_agregar.grid(row=0, column=3,padx=10, pady=5)

        
        
        self.boton_editar = tk.Button(frame, text="Editar Receta", command=self.editarReceta, image=self.imgBtn1, borderwidth=0)
        self.boton_editar.grid(row=1, column=3, padx=10, pady=5)

        self.boton_eliminar = tk.Button(frame, text="Eliminar Receta", command=self.eliminarReceta, image=self.imgBtn2, borderwidth=0)
        self.boton_eliminar.grid(row=0, column=4, padx=10, pady=5)

        self.boton_salir = tk.Button(frame, text="Salir", command=root.destroy, image=self.imgBtn3, borderwidth=0)
        self.boton_salir.grid(row=1, column=4, padx=10, pady=5)


    def agregarReceta(self):

        self.recetas = []

        

        # Agregar una nueva receta a la lista
        nuevaVentana = tk.Toplevel(root)
        nuevaVentana.geometry("400x600")

        label = tk.Label(nuevaVentana, text="Ingrese una nueva receta")
        label.grid(row=0, column=1, padx=10, pady=5)

        labelNombre = tk.Label(nuevaVentana, text="Nombre")
        labelNombre.grid(row=1, column=1, padx=10, pady=5)

        self.entryNombre = tk.Entry(nuevaVentana)
        self.entryNombre.grid(row=1, column=2, padx=10, pady=5)
        labelIngredientes = tk.Label(nuevaVentana, text="Ingredientes")

        self.textIngredientes = tk.Text(nuevaVentana)
        labelIngredientes.grid(row=2, column=1, padx=10, pady=5)
        self.textIngredientes.grid(row=2, column=2, padx=10, pady=5)
        self.textIngredientes.configure(height=10, width=15)

        labelPasos = tk.Label(nuevaVentana, text="Preparacion")
        self.textPasos = tk.Text(nuevaVentana)
        labelPasos.grid(row=3, column=1, padx=10, pady=5)
        self.textPasos.grid(row=3, column=2, padx=10, pady=5)
        self.textPasos.configure(height=10, width=15)

        labelTPrep = tk.Label(nuevaVentana, text="Tiempo de preparación")
        self.entryTPrep = tk.Entry(nuevaVentana)
        labelTPrep.grid(row=4, column=1, padx=10, pady=5)
        self.entryTPrep.grid(row=4, column=2, padx=10, pady=5)

        labelTCoccion = tk.Label(nuevaVentana, text="Tiempo de Cocción")
        self.entryTCoccion = tk.Entry(nuevaVentana)
        labelTCoccion.grid(row=5, column=1, padx=10, pady=5)
        self.entryTCoccion.grid(row=5, column=2, padx=10, pady=5)

        labelFecha = tk.Label(nuevaVentana, text="Fecha de creación")
        self.entryFecha = tk.Entry(nuevaVentana)
        labelFecha.grid(row=6, column=1, padx=10, pady=5)
        self.entryFecha.grid(row=6, column=2, padx=10, pady=5)

        self.btnGuardar = tk.Button(nuevaVentana,text="Guardar", command=self.guardar)
        self.btnGuardar.grid(row=7, column=1, padx=10, pady=5)
        
    def guardar(self):
        #Guardar datos de una nueva receta en un archivo
        nombre = self.entryNombre.get()
        ingredientes = self.textIngredientes.get("1.0", "end-1c")
        pasos = self.textPasos.get("1.0", "end-1c")
        tiempoP = self.entryTPrep.get()
        tiempoC = self.entryTCoccion.get()
        fecha = self.entryFecha.get()

        receta = {"Nombre" : nombre,
                  "Ingredientes" : ingredientes, 
                  "Pasos" : pasos,
                  "Tiempo de preparacion" : tiempoP,
                  "Tiempo de coccion" : tiempoC,
                  "Fecha de creacion" : fecha}

        self.recetas.append(receta)

        with open("recetas.json", "w") as f:
            json.dump(f"Nombre: {nombre}\n Ingredientes: {ingredientes}\n Pasos{pasos}\n Tiempo de preparacion:{tiempoP}\n Tiempo de cocción:{tiempoC}\n Fecha de creación{fecha}\n\n", f)


        with open("recetas.json", "r") as file:
            lista_leida= json.load(file)

        for elemento in lista_leida:
            self.listaRecetas.insert(tk.END, elemento)

        print("Receta guardada")

        
            
 

    def editarReceta(self):
        # Editar una receta existente de la lista

        file_path = filedialog.askopenfilename()
        with open("recetas.json", "r") as file:
            lista_leida =json.load(file)
        print(lista_leida)


            
        
        window = tk.Tk()
        window.title("Editar receta")
        text_box = tk.Text(window)
        text_box.insert("1.0", lista_leida)
        text_box.pack()

        def save_changes():
            with open(file_path, "w") as file:
                file.write(text_box.get("1.0", "end-1c"))
        save_button = tk.Button(window, text="Guardar cambios", command=save_changes)
        save_button.pack()


    def eliminarReceta(self):
        # Eliminar una receta existente de la lista
        selected_index = self.listaRecetas.curselection()
        if selected_index:
            self.listaRecetas.delete(selected_index)



root = tk.Tk()
root.geometry("800x400")
background_img = PhotoImage(file = f"background.png")
'''
canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
'''
'''
background = canvas.create_image(
    400.0, 150.0,
    image=background_img)
'''
app = AppReceta(root)
root.resizable(False, False)
root.mainloop()

