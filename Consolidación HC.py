import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button
from PIL import Image, ImageTk
import os
from datetime import datetime
from funciones import *

class MiAplicacion:

    ### Pantalla de Inicio
    def __init__(self, root):
        self.root = root
        self.root.title("Seguros Suramericana, S.A.")

        tk.Label(self.root, text="CONSOLIDACIÓN HARD CLOSE", bg="#FFFFFF", width=25, font=("Arial", 30, "bold"), fg="#001F3F").place(x=90, y=40)
        tk.Label(self.root, text="Seleccione un Módulo", bg="#FFFFFF", width=22, font=("Arial", 15), fg="#001F3F").place(x=275, y=110)
        self.transformacion = tk.Button(self.root, text="Transformación", command=self.boton_transformacion, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2").place(x=200, y=160)
        self.maduracion = tk.Button(self.root, text="Maduración", command=self.boton_maduracion, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2").place(x=450, y=160)

    ### Función para cerrar la aplicación
    def cerrar_aplicacion(self):
        self.root.destroy()
        
    ### Modulo Transformación
    def boton_transformacion(self):

        # Características de la ventana
        self.root.withdraw()
        self.ventana_transformacion = tk.Toplevel()
        self.ventana_transformacion.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        self.ventana_transformacion.focus_force()
        ancho_ventana = 800
        alto_ventana = 480
        x_pos = (self.ventana_transformacion.winfo_screenwidth() - ancho_ventana) // 2
        y_pos = (self.ventana_transformacion.winfo_screenheight() - alto_ventana) // 2
        self.ventana_transformacion.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana_transformacion['bg'] = '#FFFFFF'
        self.ventana_transformacion.resizable(0, 0)

        # Icono de SURA

        icono_path = os.path.join(os.path.dirname(__file__), "_internal/iconos", "icono.ico") #_internal/
        self.ventana_transformacion.iconbitmap(icono_path)
        self.ventana_transformacion.wm_iconbitmap(icono_path)

        # Imagen Tigre SURA
        imagen_path = os.path.join(os.path.dirname(__file__), "_internal/iconos", "tigre-sura2.jpg")
        def redimensionar_imagen(imagen_path, nuevo_tamano):
            imagen_original = Image.open(imagen_path)
            imagen_redimensionada = imagen_original.resize(nuevo_tamano)
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            return imagen_tk
        self.imagen_redimensionada = redimensionar_imagen(imagen_path, nuevo_tamano=(450, 350))
        label_imagen = tk.Label(self.ventana_transformacion, image=self.imagen_redimensionada, bd=0)
        label_imagen.pack(pady=10)
        label_imagen.place(x=0, y=160)

        # Variables necesarias para el modulo
        self.ruta_importacion = ""
        self.ruta_exportacion = ""
        
        # Elementos de la ventana
    
        # Etiqueta principal
        lbl = Label(self.ventana_transformacion, text="Transformación", bg="#FFFFFF", width=22, font=("Arial", 40, "bold"), fg="#001F3F")
        lbl.place(x=50, y=10)
        # Etiqueta descripción
        lbl = Label(self.ventana_transformacion, text="Este módulo permite tomar un listado de cuentas de Hard Close para exportarlas\nnuevamente con encabezado y sin clase de documento II o con solo encabezado.", bg="#FFFFFF", width=100, font=("Arial", 10), fg="#001F3F")
        lbl.place(x=6, y=100)
        # Botón para seleccionar la carpeta de importación
        btn_seleccionar_carpeta = Button(self.ventana_transformacion, text="Seleccionar Carpeta Importación", command=self.seleccionar_ruta1, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_seleccionar_carpeta.pack(pady=20)
        btn_seleccionar_carpeta.place(x=400, y=180)
        # Botón para seleccionar la carpeta de exportación
        btn_seleccionar_carpeta2 = Button(self.ventana_transformacion, text="Seleccionar Carpeta Exportación", command=self.seleccionar_ruta2, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_seleccionar_carpeta2.pack(pady=20)
        btn_seleccionar_carpeta2.place(x=400, y=250)
        # Botones para ejecutar el proceso
        btn_ejecutar_proceso = Button(self.ventana_transformacion, text="Encabezados y CD", command=self.ejecutar, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_ejecutar_proceso.pack(pady=20)
        btn_ejecutar_proceso.place(x=530, y=320)
        btn_ejecutar_proceso2 = Button(self.ventana_transformacion, text="Encabezados", command=self.ejecutar1, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_ejecutar_proceso2.pack(pady=20)
        btn_ejecutar_proceso2.place(x=580, y=390)
        # Botón volver
        self.boton_volver1 = tk.Button(self.ventana_transformacion, text="Volver", command=self.boton_volver_transformacion, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        self.boton_volver1.place(x=40, y=30)

    ### Modulo Maduración
    def boton_maduracion(self):

        # Características de la ventana
        self.root.withdraw()
        self.ventana_maduracion = tk.Toplevel()
        self.ventana_maduracion.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        self.ventana_maduracion.focus_force() 
        ancho_ventana = 800
        alto_ventana = 480
        x_pos = (self.ventana_maduracion.winfo_screenwidth() - ancho_ventana) // 2
        y_pos = (self.ventana_maduracion.winfo_screenheight() - alto_ventana) // 2
        self.ventana_maduracion.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana_maduracion['bg'] = '#FFFFFF'
        self.ventana_maduracion.resizable(0, 0)

        # Icono de SURA
        icono_path = os.path.join(os.path.dirname(__file__), "_internal/iconos", "icono.ico") #_internal/
        self.ventana_maduracion.iconbitmap(icono_path)
        self.ventana_maduracion.wm_iconbitmap(icono_path)

        # Imagen Tigre SURA
        imagen_path = os.path.join(os.path.dirname(__file__), "_internal/iconos", "tigre-sura.jpg")
        def redimensionar_imagen(imagen_path, nuevo_tamano):
            imagen_original = Image.open(imagen_path)
            imagen_redimensionada = imagen_original.resize(nuevo_tamano)
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            return imagen_tk
        imagen_redimensionada = redimensionar_imagen(imagen_path, nuevo_tamano=(400, 300))
        label_imagen = tk.Label(self.ventana_maduracion, image=imagen_redimensionada, bd=0)
        label_imagen.pack(pady=10)
        label_imagen.place(x=380, y=260)

        # Variables necesarias para el modulo
        self.fecha_corte = tk.StringVar(value='')
        self.archivo_salida = tk.StringVar(value='')
        self.ruta_importacion = ""
        self.ruta_exportacion = ""
        
        ## Elementos de la ventana

        # Etiqueta principal
        lbl = Label(self.ventana_maduracion, text="Maduración", bg="#FFFFFF", width=22, font=("Arial", 40, "bold"), fg="#001F3F")
        lbl.place(x=50, y=10)
        # Etiqueta descripción
        lbl = Label(self.ventana_maduracion, text="Este módulo permite tomar un listado de cuentas de Hard Close para calcular su nivel de maduración.\n", bg="#FFFFFF", width=100, font=("Arial", 10), fg="#001F3F")
        lbl.place(x=6, y=110)
        # Etiqueta fecha corte
        lbl = Label(self.ventana_maduracion, text="Ingrese Fecha de Corte (Formato AAAA/MM/DD):", bg="#FFFFFF", font=("Arial", 15, "bold"), fg="#001F3F")
        lbl.place(x=60, y=170)
        # Etiqueta archivo salida
        lbl = Label(self.ventana_maduracion, text="Ingrese un Nombre para el Archivo de Salida:", bg="#FFFFFF", font=("Arial", 15, "bold"), fg="#001F3F")
        lbl.place(x=60, y=220)
        # Cuadro de texto para fecha de corte
        self.box_fecha_corte = tk.Entry(self.ventana_maduracion, textvariable=self.fecha_corte, width=15, font=("Arial", 15, "bold"), bd=2, fg='gray')
        self.box_fecha_corte.pack(pady=10)
        self.box_fecha_corte.place(x=550, y=170)
        # Cuadro de texto para nombre del archivo de salida
        self.box_archivo_salida = tk.Entry(self.ventana_maduracion, textvariable=self.archivo_salida, width=15, font=("Arial", 15, "bold"), bd=2, fg='gray')
        self.box_archivo_salida.pack(pady=10)
        self.box_archivo_salida.place(x=550, y=220)
        # Botón para seleccionar la carpeta de importación
        btn_seleccionar_carpeta = Button(self.ventana_maduracion, text="Seleccionar Carpeta Importación", command=self.seleccionar_ruta3, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_seleccionar_carpeta.pack(pady=20)
        btn_seleccionar_carpeta.place(x=60, y=270)
        # Botón para seleccionar la carpeta de exportación
        btn_seleccionar_carpeta2 = Button(self.ventana_maduracion, text="Seleccionar Carpeta Exportación", command=self.seleccionar_ruta4, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        btn_seleccionar_carpeta2.pack(pady=20)
        btn_seleccionar_carpeta2.place(x=60, y=330)
        # Botón para ejecutar el proceso
        btn_ejecutar_proceso = Button(self.ventana_maduracion, text="Ejecutar Proceso", command=self.ejecutar2, bg="#001F3F", fg="#FFFFFF", font=("Arial", 20, "bold"), bd=0, cursor="hand2")
        btn_ejecutar_proceso.pack(pady=20)
        btn_ejecutar_proceso.place(x=60, y=390)
        # Botón volver
        self.boton_volver2 = Button(self.ventana_maduracion, text="Volver", command=self.boton_volver_maduracion, bg="#001F3F", fg="#FFFFFF", font=("Arial", 15, "bold"), bd=0, cursor="hand2")
        self.boton_volver2.place(x=40, y=30)

        self.ventana_maduracion.mainloop()

    ## Funciones para ejecutar Transformación

    # Función para seleccionar ruta de importación
    def seleccionar_ruta1(self):
        self.ruta_importacion = filedialog.askdirectory()
        print(f"Ruta de importación: {self.ruta_importacion}.")
    # Función para seleccionar ruta de exportación
    def seleccionar_ruta2(self):
        self.ruta_exportacion = filedialog.askdirectory()
        print(f"Ruta de exportación: {self.ruta_exportacion}.")
    # Funciones para procesar los archivos en la ruta de importación
    def ejecutar(self):
        if self.ruta_importacion and self.ruta_exportacion:   
            try:
                transformacion(self.ruta_importacion, self.ruta_exportacion)
                print("Proceso ejecutado con éxito.")   
            except Exception as e:
                print(f"Error con los archivos importados: {e}")
        else:
            print("Por favor, ingrese todos los parámetros.")

    def ejecutar1(self):
        if self.ruta_importacion and self.ruta_exportacion:   
            try:
                transformacion2(self.ruta_importacion, self.ruta_exportacion)
                print("Proceso ejecutado con éxito.")   
            except Exception as e:
                print(f"Error con los archivos importados: {e}")
        else:
            print("Por favor, ingrese todos los parámetros.")

    ## Funciones para ejecutar Maduración

    # Función para almacenar la fecha de corte
    def fecha_corte_func(self):
        self.fecha_corte = self.box_fecha_corte.get()
    # Función para almacenar el nombre de archivo
    def archivo_salida_func(self):
        self.archivo_salida = self.box_archivo_salida.get()
    # Función para seleccionar ruta de importación
    def seleccionar_ruta3(self):
        self.ruta_importacion = filedialog.askdirectory()
        print(f"Ruta de importación: {self.ruta_importacion}.")
    # Función para seleccionar ruta de exportación
    def seleccionar_ruta4(self):
        self.ruta_exportacion = filedialog.askdirectory()
        print(f"Ruta de exportación: {self.ruta_exportacion}.")
    # Función para procesar los archivos en la ruta de importación
    def ejecutar2(self):
        self.fecha_corte_func()
        self.archivo_salida_func()
        if self.fecha_corte and self.archivo_salida and self.ruta_importacion and self.ruta_exportacion:   
            try:
                fecha_valida = datetime.datetime.strptime(self.fecha_corte, '%Y/%m/%d')
                self.fecha_corte = fecha_valida
                print("Fecha válida:", self.fecha_corte)
            except ValueError:
                print("Error: La fecha ingresada no tiene el formato AAAA/MM/DD. No se puede ejecutar el proceso.")
                return
            try:
                maduracion(self.fecha_corte, self.archivo_salida, self.ruta_importacion, self.ruta_exportacion)
                print("Proceso ejecutado con éxito.")   
            except Exception as e:
                print(f"Error con los archivos importados: {e}")
        else:
            print("Por favor, ingrese todos los parámetros.")

    ### Botones volver de modulos transformación y maduración
    def boton_volver_transformacion(self):
        self.ventana_transformacion.withdraw()
        self.root.deiconify()
        

    def boton_volver_maduracion(self):
        self.ventana_maduracion.withdraw()
        self.root.deiconify()

### Características de la ventana principal
root = tk.Tk()
ancho_ventana = 800
alto_ventana = 480
x_pos = (root.winfo_screenwidth() - ancho_ventana) // 2
y_pos = (root.winfo_screenheight() - alto_ventana) // 2
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
root['bg'] = '#FFFFFF'
root.resizable(0, 0)

# Icono de SURA
root.iconbitmap("_internal/iconos/icono.ico") #_internal/
root.wm_iconbitmap("_internal/iconos/icono.ico")

# Logo SURA Seguros
imagen_path = "_internal/iconos/tigre-sura.jpg"
def redimensionar_imagen(imagen_path, nuevo_tamano):
    imagen_original = Image.open(imagen_path)
    imagen_redimensionada = imagen_original.resize(nuevo_tamano)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    return imagen_tk
imagen_redimensionada = redimensionar_imagen(imagen_path, nuevo_tamano=(400, 300))
label_imagen = tk.Label(root, image=imagen_redimensionada, bd=0)
label_imagen.pack(pady=10)
label_imagen.place(x=200, y=220)

### Inicializar la aplicación
app = MiAplicacion(root)

### Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()