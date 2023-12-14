
import turtle
import winsound

# Función para cambiar el color de las paletas
def cambiar_color_pared(pared, color):
    pared.color(color)

# Función para cambiar la forma y el color de la pelota
def cambiar_forma_y_color_pelota(pelota, forma, color):
    pelota.shape(forma)
    pelota.color(color)

# Inicializa la pantalla de Turtle
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=1920, height=1080)

# Crea dos objetos Turtle para ingresar los nombres
nombre1_input = turtle.textinput("INGRESAR", "JUGADOR 1:")
nombre2_input = turtle.textinput("INGRESAR", "JUGADOR 2:")

# Asigna los nombres ingresados a las variables
nombre1 = nombre1_input
nombre2 = nombre2_input

# Menú de selección de forma y color de la pelota
forma_pelota = ventana.textinput("Configurar pelota", "Ingresa la forma de la pelota (circle, square, triangle, etc.):")
color_pelota = ventana.textinput("Configurar pelota", "Ingresa el color de la pelota (ej. white):")

# Menú de selección de color de las paletas
color_pared = ventana.textinput("Configurar paletas", "Ingresa el color de las paletas (ej. white):")

# Pared izquierda
pared_izquierda = turtle.Turtle()
pared_izquierda.speed(0)
pared_izquierda.shape("square")
cambiar_color_pared(pared_izquierda, color_pared)
pared_izquierda.shapesize(stretch_wid=5, stretch_len=1)
pared_izquierda.penup()
pared_izquierda.goto(-950, 0)

# Pared derecha
pared_derecha = turtle.Turtle()
pared_derecha.speed(0)
pared_derecha.shape("square")
cambiar_color_pared(pared_derecha, color_pared)
pared_derecha.shapesize(stretch_wid=5, stretch_len=1)
pared_derecha.penup()
pared_derecha.goto(935, 0)

# Pelota en forma de círculo
pelota = turtle.Turtle()
pelota.speed(40)
cambiar_forma_y_color_pelota(pelota, forma_pelota, color_pelota)
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2
pelota.dy = -2

# Marcador
puntaje_izquierda = 0
puntaje_derecha = 0
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 450)
marcador.write(f"{nombre1}: 0   {nombre2}: 0", align="center", font=("Courier", 24, "normal"))

# Funciones para mover las paredes arriba y abajo
def pared_izquierda_arriba():
    y = pared_izquierda.ycor()
    if y < 400:
        y += 20
        pared_izquierda.sety(y)

def pared_izquierda_abajo():
    y = pared_izquierda.ycor()
    if y > -380:
        y -= 20
        pared_izquierda.sety(y)

def pared_derecha_arriba():
    y = pared_derecha.ycor()
    if y < 400:
        y += 20
        pared_derecha.sety(y)

def pared_derecha_abajo():
    y = pared_derecha.ycor()
    if y > -380:
        y -= 20
        pared_derecha.sety(y)

# Esta línea de código indica que el juego está escuchando eventos del teclado.
# Esto es necesario para que el juego pueda "capturar" las teclas que el usuario está presionando.
ventana.listen()
ventana.onkeypress(pared_izquierda_arriba, "w")
ventana.onkeypress(pared_izquierda_abajo, "s")
ventana.onkeypress(pared_derecha_arriba, "Up")
ventana.onkeypress(pared_derecha_abajo, "Down")

# Variable de velocidad de la pelota
velocidad_pelota = 2

# Función para aumentar la velocidad de la pelota
def aumentar_velocidad():
    global velocidad_pelota
    velocidad_pelota += 0

# Bucle principal del juego
while True:
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx * velocidad_pelota)
    pelota.sety(pelota.ycor() + pelota.dy * velocidad_pelota)

    # Comprobación de bordes para las paredes superior e inferior
    if pelota.ycor() > 490 or pelota.ycor() < -490:
        pelota.dy *= -1
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)  # Reemplaza "boing.wav" con tu efecto de sonido

    # Comprobación de bordes para las paredes izquierda y derecha
    if pelota.xcor() > 940:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje_izquierda += 1
        aumentar_velocidad()  # Aumenta la velocidad
        marcador.clear()
        marcador.write(f"{nombre1}: {puntaje_izquierda}   {nombre2}: {puntaje_derecha}", align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -940:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje_derecha += 1
        aumentar_velocidad()  # Aumenta la velocidad
        marcador.clear()
        marcador.write(f"{nombre1}: {puntaje_izquierda}   {nombre2}: {puntaje_derecha}", align="center", font=("Courier", 24, "normal"))

    # Detección de colisión entre la pelota y las paredes izquierda y derecha
    if (     
        pelota.xcor() > 930 and pelota.distance(pared_derecha) < 50 
    ) or (     
        pelota.xcor() < -930 and pelota.distance(pared_izquierda) < 50 
    ):     
        pelota.dx *= -1    
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)  # Reemplaza "boing.wav" con tu efecto de sonido

ventana.bye()
