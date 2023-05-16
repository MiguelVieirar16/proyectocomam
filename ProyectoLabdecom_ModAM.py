from tkinter import*
import tkinter as tk
from tkinter import messagebox, ttk
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy import signal


#Holaa
root = tk.Tk()
root.geometry("750x420+100+100")
root.title("GENERADOR :)")
root.resizable(False, False)
root.configure(background='black')

def valida_fre(frecuencia_str):
    if frecuencia_str.isdigit():
        return True
    else:
        return False
               
def valida_amp(a_str):

    if a_str.isdigit():
        return True
    else:
         return False  
    
t_s = np.linspace (0,1,1000)
A_sm = 5 #amplitud de la portadora
f_sm = 4000 #frecuencia de la moduladora
t = np.linspace(0, 1, 1000, endpoint = True) #Onda Cuadrada
ka = 2 #indice de modulacion 

frecuencia_usuario = tk.Label(root, text="Frecuencia",bg="black" , fg="white").place(x=80,y=305)
frecuencia_usuario = tk.Entry(root, validate = "key", validatecommand = (root.register(valida_fre), '%P'),borderwidth= 2,)
frecuencia_usuario.pack
frecuencia_usuario.place(x=80,y=327)

amplitud_usuario = tk.Label(root, text="Amplitud",bg="black" , fg="white").place(x=80,y=355)
amplitud_usuario = tk.Entry(root, validate = "key", validatecommand = (root.register(valida_amp), '%P'),borderwidth= 2,)
amplitud_usuario.pack()
amplitud_usuario.place(x=80,y=377)


def Mensaje () :

    
    moduladora = A_sm*np.cos(2*np.pi*f_sm*t_s)
    plt.title('Señal de Mensaje 4KHz')
    plt.plot(moduladora,'g')
    plt.ylabel('Amplitud')
    plt.show()





# Icono de la ventana.
#root.iconbitmap("D:\img3.ico")

# //Fondo de la ventana.//
#imagen = PhotoImage(file="D:\img2.png")
#Label(root, image=imagen, bd=0).pack()

# //GENERANDO ONDA.//
onda = LabelFrame(root, width=280, height=280, text="ONDA", font=('Comic Sans Ms', 14, 'bold'), fg="White", bg="black", border=5)
onda.place(x=40, y=10) #'Verdana' / 'Comic Sans Ms'
name = Label(onda, text="Seleccione el tipo de onda:", font=('Comic Sans Ms', 12), fg="White", bg="Black")
name.place(x=20, y=15)

combo = ttk.Combobox(onda, state="readonly", values=["SINUSOIDAL","CUADRADA"], font=('Comic Sans Ms', 12), width=20, height=50)
combo.place(x=20, y=40)


def datos():
    global amp, frc
    comb = combo.get()
    if (comb == "SINUSOIDAL") or (comb == "CUADRADA") :

        if comb == "SINUSOIDAL" :
            frecuencia_str = frecuencia_usuario.get()
            a_str = amplitud_usuario.get()

            if frecuencia_str == '' or a_str == '':
                tk.messagebox.showerror('Error', 'Para mostrar la onda, debe ingresar una frecuencia y una Amplitud')
                return
            
            f_sp = float(frecuencia_str) #frecuencia de la portadora
            A_sp = float(a_str) #amplitud de la moduladora
            portadora = A_sp*np.cos(2*np.pi*f_sp*t_s)   
            plt.clf()
            plt.title('Señal de Portadora')
            plt.plot(portadora,'r')
            plt.ylabel('Amplitud')  

            plt.show()
        else:
            plt.clf()
            plt.plot(t, signal.square(2 * np.pi * 5 * t))
            plt.ylabel('Amplitud')
            plt.title('Onda Cuadrada')
            plt.show()
            


    else:
        messagebox.showinfo(message= "Por favor, seleccione una opción :)", title="Aviso")

#def clear():
        
def grafica():
    # Nueva ventana donde se visualizará la gráfica.
    ventana2 = Tk()
    ventana2.geometry("650x300")
    ventana2.title("GRÁFICA📉")
    ventana2.resizable(False, False) 
    # Icono de la ventana.
    ventana2.iconbitmap("C:/Users/eliki/OneDrive/Escritorio/FrontEnd Project/img3.ico")
    onda1 = Label(ventana2, text=f"ONDA {combo.get()}", font=('Comic Sans Ms', 14), justify='center').place(x=40,y=5)
    
# Botón Aceptar
button0= ttk.Button(onda, text="Aceptar", command=datos)
button0.place(x=88, y=80)
button4= ttk.Button(onda, text="Mensaje", command=Mensaje)
button4.place(x=88, y=110)

# //GENERANDO MODULACIÓN.//

mod = LabelFrame(root, width=300, height=180, text="MODULACIÓN", font=('Comic Sans Ms', 12, 'bold'), fg="White", bg="Black", border=5)
mod.place(x=390, y=25)
name = Label(mod, text="Seleccione el tipo de modulación:", font=('Comic Sans Ms', 12), fg="White", bg="Black")
name.place(x=20, y=15)
combo1 = ttk.Combobox(mod, state="readonly", values=["AM"], font=('Comic Sans Ms', 12), width=20, height=50)
combo1.place(x=25, y=40)

def grafica2():
    comb = combo1.get()
   

    if (comb == "AM") :
        frecuencia_str = frecuencia_usuario.get()
        a_str = amplitud_usuario.get()


        if frecuencia_str == '' or a_str == '':
            tk.messagebox.showerror('Error', 'Debe ingresar una frecuencia y una Amplitud')
            return

        f_sp = float(frecuencia_str) #frecuencia de la portadora
        A_sp = float(a_str) #amplitud de la moduladora
        modulacion_AM = A_sp*(1+ka*np.cos(2*np.cos(2*np.pi*f_sm*t_s))*np.cos(2*np.pi*f_sp*t_s))
       
        plt.clf()
        plt.title('Modulacion AM')
        plt.plot(modulacion_AM, color="purple")
        plt.ylabel('Amplitud')
        plt.xlabel('Señal AM')
        plt.show()
       
    else:
        messagebox.showinfo(message= "Por favor, seleccione una opción 💃", title="Aviso")

button3= ttk.Button(mod, text="Modular", command=grafica2)
button3.place(x=100, y=80)


def comparar():
    
    frecuencia_str = frecuencia_usuario.get()
    a_str = amplitud_usuario.get()
    f_sp = float(frecuencia_str) #frecuencia de la portadora
    A_sp = float(a_str) #amplitud de la moduladora
    modulacion_AM = A_sp*(1+ka*np.cos(2*np.cos(2*np.pi*f_sm*t_s))*np.cos(2*np.pi*f_sp*t_s))
    portadora = A_sp*np.cos(2*np.pi*f_sp*t_s)  
    moduladora = A_sm*np.cos(2*np.pi*f_sm*t_s) 

    plt.clf()

    plt.subplot(4,1,1)
    plt.title('Señal de Mensaje o Moduladora')
    plt.plot(moduladora,'g')
    plt.ylabel('Amplitud')

    #Señal de Portadora
    plt.subplot(4,1,2)
    plt.title('Señal de Portadora')
    plt.plot(portadora,'r')
    plt.ylabel('Amplitud')

    #Señal AM
    plt.subplot(4,1,3)
    plt.title('Modulacion AM')
    plt.plot(modulacion_AM, color="purple")
    plt.ylabel('Amplitud')
    plt.xlabel('Señal AM')

    plt.subplot(4,1,4)
    plt.plot(t, signal.square(2 * np.pi * 5 * t))
    plt.ylabel('Amplitud')
    plt.title('Onda Cuadrada')
   
    plt.show()

button5= tk.Button(root, text="Comparar", command=comparar)
button5.configure(background='Black',font='Segoe ',fg='Red')
button5.place(x=500, y=300)

root.mainloop()