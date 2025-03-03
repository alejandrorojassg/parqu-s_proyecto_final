
from tkinter import Tk, Label, Button, Entry, StringVar, Canvas, Toplevel, Event
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen, Turtle
from PIL import Image, ImageTk 
from PIL import Image, ImageTk
import random


parques_interfaz = Tk()                                  #Creación de la ventana principal.
parques_interfaz.title("Parqués Python")
parques_interfaz.geometry("1430x800")                    #Dimensiones de la ventana TK. 
#creación de la ventana secundaria que contiene el juego mediante la imagén.
parques_secundario = Canvas(parques_interfaz,width=800,height = 480)
parques_secundario.pack()
parques_juego= TurtleScreen(parques_secundario)
parques_juego.bgcolor("beige")
parques_anidado = RawTurtle(parques_juego)
parques_anidado.speed(3)

estructura_parques = Image.open("tablero_parques.png")    #Abriendo la imagen del directorio.
estructura_parques = estructura_parques.convert("RGBA")      #Transformando el formato de la imagén a RGBA
estructura_parques = estructura_parques.resize((800,480))    #Redimensionando la imagén.
estructura = ImageTk.PhotoImage(estructura_parques)          #Incrustar la imagén en la ventana
parques_secundario.create_image(0,0,image=estructura)         


mensaje = Label(parques_interfaz, text = "Hola!, Bienvenido al juego de mesa parqués. Presiona el botón para continuar.", fg = "blue", bg = "yellow"
                )
mensaje.pack(
)
mensaje.place(x =500, y = 680, height = 50
              )


mensaje_jugadores = Label(parques_interfaz, text="Ingresa el número de jugadores(máximo 4):", fg = "blue"
                          )
mensaje_jugadores.pack(
)
mensaje_jugadores.place(x = 580, y= 560,height = 20 
                        )

jugadores_verdes = ["jugador_verde1","jugador_verde2","jugador_verde3","jugador_verde4"]
jugador_verde1=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="green", width= 1, tags="jugador_verde1")
jugador_verde2=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="green", width= 1, tags="jugador_verde2")
jugador_verde3=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="green", width= 1, tags="jugador_verde3")
jugador_verde4=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="green", width= 1, tags="jugador_verde4")
parques_secundario.move("jugador_verde1",150,-220)
parques_secundario.move("jugador_verde2",250,-220)
parques_secundario.move("jugador_verde3",250,-280)
parques_secundario.move("jugador_verde4",150,-280)


jugadores_azules = ["jugador_azul1","jugador_azul2","jugador_azul3","jugador_azul4"]
jugador_azul1=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="blue", width= 1, tags="jugador_azul1")
jugador_azul2=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="blue", width= 1, tags="jugador_azul2")
jugador_azul3=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="blue", width= 1, tags="jugador_azul3")
jugador_azul4=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="blue", width= 1, tags="jugador_azul4")
parques_secundario.move("jugador_azul1",-300,-220)
parques_secundario.move("jugador_azul2",-400,-220)
parques_secundario.move("jugador_azul3",-405,-280)
parques_secundario.move("jugador_azul4",-300,-280)



jugadores_amarillos =["jugador_amarillo1","jugador_amarillo2","jugador_amarillo3","jugador_amarillo4"]
jugador_amarillo1=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="yellow", width= 1, tags="jugador_amarillo1")
jugador_amarillo2=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="yellow", width= 1, tags="jugador_amarillo2")
jugador_amarillo3=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="yellow", width= 1, tags="jugador_amarillo3")
jugador_amarillo4=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="yellow", width= 1, tags="jugador_amarillo4")
parques_secundario.move("jugador_amarillo1",-300,70)
parques_secundario.move("jugador_amarillo2",-400,70)
parques_secundario.move("jugador_amarillo3",-400,120)
parques_secundario.move("jugador_amarillo4",-300,120)


jugadores_rojos = ["jugador_rojo1","jugador_rojo2","jugador_rojo3","jugador_rojo4"]
jugador_rojo1=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="red", width= 1, tags="jugador_rojo1")
jugador_rojo2=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="red", width= 1, tags="jugador_rojo2")
jugador_rojo3=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="red", width= 1, tags="jugador_rojo3")
jugador_rojo4=parques_secundario.create_oval(86,86,60,60, outline ="black", fill ="red", width= 1, tags="jugador_rojo4")
parques_secundario.move("jugador_rojo1",527,1)
parques_secundario.move("jugador_rojo2",645,-20)
parques_secundario.move("jugador_rojo3",630,50)
parques_secundario.move("jugador_rojo4",30,50)


turno_actual = StringVar()    
indice_turno = 0

jugadores = ["Jugador Rojo", "Jugador Azul", "Jugador Amarillo", "Jugador Verde"]

jugadores_fichas = [jugador_rojo1,jugador_rojo2,jugador_rojo3,jugador_rojo4,jugador_azul1,jugador_azul2,jugador_azul3,jugador_azul4,
                    jugador_amarillo1,jugador_amarillo2,jugador_amarillo3,jugador_amarillo4,jugador_verde1,jugador_verde2,jugador_verde3,jugador_verde4]
fichas_carcel = []
fichas_carcel.append(jugadores_fichas)
fichas = []


tablero = [(400,400,400,400),(400,400,400,400),
           (400,400,400,400),(400,400,400,400)]


#Definición del dado

dado_ventana = None

#definición de la función del dado.
def dado ():
    """Función que determina la cantidad de pasos que se recorren con los dados creados
    aleatoriamente"""

    global dado
    global resultado_1
    global resultado_2
    dado_uno = list(range(1,7)
                )
    dado_dos = list(range(1,7)
                )
    resultado_1 = random.choice(dado_uno
                                    )
    resultado_2 = random.choice(dado_dos
                                     )

    ficha_aviso = Label(parques_interfaz, text = f"{jugadores[indice_turno]} Puede sacar una ficha",state="disabled", font =("Roboto",12), fg = "blue")
    ficha_aviso.pack()
    ficha_aviso.place(x=20,y=60)
    

    global abrir_ventana_dados
    if resultado_1 == resultado_2:
        if fichas_carcel[turno_actual.get()] == []:
            sacar_ficha.config(state ="normal")
            ficha_aviso = Label(parques_interfaz, text = f"{jugadores[indice_turno]} Puede sacar una ficha", font =("Roboto",12), fg = "blue", state="normal")
            ficha_aviso.pack()
            ficha_aviso.place(x=20,y=60)
        else:
            ficha_aviso.config(text = f"{jugadores[indice_turno]}ya no tiene fichas en la carcel, no puede sacar una ficha")
            sacar_ficha.config(state="disabled")

    return resultado_1 + resultado_2

def abrir_ventana_dados():
    """"Abre la una ventana en el momento en que se tiran los dados
    para avisar el resultado de los dados y la cantidad de pasos que se recorren.
    """
    dados = dado() 
    global dado_ventana
    dado_ventana = Toplevel(parques_interfaz)
    dado_ventana.title("Resultado dados")
    dado_ventana.geometry("480x300")
    aviso_dados = Label(dado_ventana, text=f"Los dados dieron {resultado_1} y {resultado_2} lo que es igual a= {dados} pasos", font =("Roboto",12), fg = "blue")
    aviso_dados.pack()
    aviso_dados.place(x =50, y=50)
    cerrar_aviso_dados = Button(dado_ventana, text = "Okay, gracias", font =("Roboto",12), command = cerrar_aviso_dados1)
    cerrar_aviso_dados.pack()
    cerrar_aviso_dados.place(x = 100, y = 200)
    tirar_dados.config(state="disabled")
    global cambiar_turno

def cambiar_turno():
    """Permite cambiar el turno de los jugadores de manera automática"""
    global indice_turno
    global turno_jugador
    terminar_turno.config(state = "active")
    indice_turno = (indice_turno + 1) % len(jugadores)
    turno_jugador.config(text = f"Turno del {jugadores[indice_turno]}")

def cerrar_aviso_dados1():
    """Cierra el aviso de la ventana de los dados y permite que se pueda tirar los dados 
    nuevamente"""

    global dado_ventana
    if dado_ventana is not None :
        dado_ventana.destroy()
        dado_ventana = None
    tirar_dados.config(state="active")



def cambiar_turnos():
    """""La función que anida otras que al correr permite cambiar el turno del jugador libremente
    """
    global cambiar_turnos
    cerrar_aviso_dados1()
    salida_carcel()



adver = StringVar()
advertencia = Label(parques_interfaz, textvariable = adver)
#Creación de una entrada para ingresar el número de jugadores.
jugadores_num = Entry(parques_interfaz, bg = "beige"
                      )
jugadores_num.place(x = 550, y= 590,height= 50, width =300
                    )
adver = StringVar(
)   #El StringVar determina un mensaje emergente que puede cambiar.
#Creación de el mensaje emergente que cambia según la variable adver con un if
advertencia = Label(parques_interfaz, textvariable = adver
                    )
advertencia.pack()
advertencia.place(x =600, y=640, height=20, width=200
                  )


def presionar_parajugar ():
    """""Cuando el número de jugadores es correcto se abre la ventana de juego
    y se da paso al boton para empezar a jugar y da paso al juego"""

    try:
        num = int(jugadores_num.get())
        if 2<=num<=4:
            adver.set("El número de jugadores es correcto")  #Aviso emergente de que el número de jugadores es correcto
            jugador.destroy()    #Destrucción del botón de ingresar el número de jugadores.
            #Creación de el botón para empezar a jugar    
            jugar = Button(parques_interfaz, text = "Presione para jugar",font =("Roboto",12),
               )
            jugar.pack(
            )
            jugar.place(x=550,y=490, height=40, width = 300
            )
            global empieza_el_juego    #Declaración global de la función "empieza_el_juego"
            def empieza_el_juego(evento):
                """Se destruye la interfaz inicial para dar paso al verdadero juego creando
                otra interfaz nueva para mover las fichas, terminar turnos y tirar dados"""
                global indice_turno #Declaración global de la variable "indice_turno"
                #Abre paso al juego destruyendo los botones y mensajes de la interfaz inicial
                jugadores_num.destroy()
                jugador.destroy()
                mensaje.destroy()
                mensaje_jugadores.destroy()
                advertencia.destroy()
                global turno_jugador   #Declaración global de la variable "turno_jugador"
                #Definición del mensaje que avisa cada turno de los jugadores y los cambios que tienen.
                turno_jugador = Label(parques_interfaz, text = f"Turno del {jugadores[indice_turno]}", font =("Roboto",12), fg = "blue")
                turno_jugador.pack()
                turno_jugador.place(x=300, y=700 ,height=40)
                if jugar.winfo_exists() == True:     #Creación de un if que destruye el botón "Presione para jugar" siempre y cuando este se encuentre en la ventana
                    jugar.destroy()         
                global terminar_juego
                global tirar_dados   #Declaración global de la variable "tirar dados"
                #Definición del botón que permite al jugador tirar los dados y crear una ventana emergente
                #que avise el resultado de los dados y a que jugador le corresponde.
                tirar_dados = Button(parques_interfaz, text = "Tirar los dados",height = 40, font =("Roboto",12), command =abrir_ventana_dados , bg ="blue", fg="white")
                tirar_dados.pack()
                tirar_dados.place(x =315,y=500, height=60,width = 200)
                #Se crea un botón que permite al jugador terminar la partida, en conclusión, cerrar la ventana.
                terminar_juego = Button(parques_interfaz, text = "Presione para terminar la partida",command = terminar_el_juego,height = 40, font =("Roboto",12), bg="red", fg="white")
                terminar_juego.pack()
                terminar_juego.place(x =1140,y=700,height=60,width = 280)
                global sacar_ficha         #Declaración global de la variable "sacar ficha"
                #Se crea un boton que permite al jugador sacar la ficha de la carcel cuando se cumplan las condiciones.
                sacar_ficha = Button(parques_interfaz, text ="Escoja la ficha que desea sacar de la carcel", font =("Roboto",12), bg="blue", fg="white", state = "disabled")
                sacar_ficha.pack()
                sacar_ficha.place(x =679, y=500 ,height=55, width= 350)
                global terminar_turno   #declaración global de la variable "terminar turno"
                #Se crea un boton que termina el turno de el jugador en cuestión.
                terminar_turno = Button(parques_interfaz, text = f"{jugadores[indice_turno]}, presione para terminar su turno", font =("Roboto",10), bg="blue", fg="white", state = "active", command = cambiar_turno)
                terminar_turno.pack()
                terminar_turno.place(x = 10, y = 400, height = 40, width = 300)
                
            jugar.bind("<Button-1>",empieza_el_juego)      #Se da paso al juego mediante la acción de apretar el boton "jugar"
        else:
            adver.set("El número de jugadores es incorrecto")
    except ValueError:             #Si el numero de jugadores no es un entero no será una entrada valida y por ende 
                                   #resulta en un ValueError
        adver.set("Ingrese el número de jugadores valido")
    return 

def terminar_el_juego():
    """Se destruye la ventana de juego y por ende termina"""""
    parques_interfaz.destroy()


jugador = Button(parques_interfaz, text = "Presione para ingresar la cantidad de jugadores",font =("Roboto",10),command = presionar_parajugar
               )
jugador.pack(  
)    #Definición del boton que permite ingresar la cantidad de jugadores.
jugador.place(x=550,y=490, height=40, width = 300)        #Posicionamiento del boton en la ventana desplegada.

centro =parques_secundario.create_oval(150,70,100,100, fill = "violet", tags="circulo", outline=""
                        )      #Creación del circulo central que definirá la "llegada" del jugador
parques_secundario.coords("circulo",110,68,-117,-70)     #Posicionamiento dle circulo central mediante coordenadas x1, x2, y1, y2

equipo_azul_parques_ = parques_secundario.create_rectangle(400,400,200,200, fill = "", tags="equipo_azul", outline ="black"
                        )      #Creación del cuadrado que define al equipo azul y actuará como carcel del equipo azul.
parques_secundario.coords("equipo_azul",-390,-110,-178,-230 )     #Posicionamiento del cuadrado y carcel del equipo azul
                                                                 #mediante coordenadas x1, x2, y1, y2

equipo_rojo_parques = parques_secundario.create_rectangle(80,80,80,80, fill = "", tags="equipo_rojo", outline ="black"
                        ) #Creación del cuadrado que define al equipo rojo y actuará como carcel del equipo rojo.
parques_secundario.coords("equipo_rojo",390,110,178,230 ) #Posicionamiento del cuadrado y carcel del equipo rojo
                                                           #mediante coordenadas x1, x2, y1, y2


equipo_verde_parques = parques_secundario.create_rectangle(80,80,80,80, fill = "", tags="equipo_verde", outline="black"
                            )    #Creación del cuadrado que define al equipo verde y actuará como carcel del equipo verde
parques_secundario.coords("equipo_verde", 390,-110,178,-230) #Posicionamiento del cuadrado y carcel del equipo verde
                                                               #mediante coordenadas x1, x2, y1, y2

equipo_amarillo_parques = parques_secundario.create_rectangle(80,80,80,80, fill = "", tags="equipo_amarillo", outline="black"
                            ) #Creación del cuadrado que define al equipo amarillo y actuará como carcel del equipo amarillo
parques_secundario.coords("equipo_amarillo", -390,110,-178,230)  #Posicionamiento del cuadrado y carcel del equipo amarillo
                                                                 #mediante coordenadas x1, x2, y1, y2

parques_secundario.move("jugador_rojo1",-370,68)     #Posicionamiento de las fichas de los jugadores
parques_secundario.move("jugador_rojo2",-390,90)
parques_secundario.move("jugador_rojo3",-370,68)
parques_secundario.move("jugador_rojo4",130,68)


casilla_1 = parques_secundario.create_rectangle(90,85,10,60, fill="white", tags="casilla_1", outline="black")
parques_secundario.move("casilla_1", 100,160 )



parques_interfaz.mainloop(

)
