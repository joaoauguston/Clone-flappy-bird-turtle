
# horse Jump

import turtle
import time                         # importa o módulo para usar o tempo no jogo

# janela do jogo
cenario = turtle.Screen()  # criação da tela
cenario.title("Horse Jump")  # titulo da janela
cenario.bgcolor("lightblue")  # cor de fundo
cenario.bgpic("fundo.gif")  # colocar a imagem de fundo
cenario.setup(width=500, height=800)  # Configuração da tela
cenario.tracer(0)  # Esta função é usada para ligar ou desligar a animação

# escrita do placar
placar = turtle.Turtle()  # chamamos o modulo turtle
placar.speed(0)  # A velocidade que desenha o placar na tela
# Para desenhar o nosso placar de forma "ivisivel"
placar.hideturtle()
placar.penup()  # levanta a caneta
placar.color("white")  # A cor da fonte do placar
placar.goto(0, 250)  # Posição do placar
placar.write("0", move=False, align="left", font=(
    "Arial", 32, "normal"))  # dados do nosso placar


# Criação do personagem
turtle.register_shape('cavalo.gif')      # chamando a imagem
cavalo = turtle.Turtle('cavalo.gif')     # chamado da imagem na variavel cavalo
# A velocidade que ele é exibida na tela
cavalo.speed(0)
cavalo.penup()                           # tira a caneta
# Definimos nossa tartaruga com a imagem cavalo gif
cavalo.shape('cavalo.gif')
# Posição do nosso cavalo na tela de exibição
cavalo.goto(-100, 0)  # manda o cavalo para as coordenadas (-100, 0) : (X, Y)
cavalo.dx = 0                            # é o posicionamento em relação ao eixo X
# é o posicionamento em relação ao eixo Y ( é oque faz o cavalo subir )
cavalo.dy = 0

# obstaculos

# registra imagens do cone e da cobra
turtle.register_shape('cone.gif')
turtle.register_shape('cobra.gif')

# Criação da cobra 1
cobra1 = turtle.Turtle('cobra.gif')  # adiciona imagem da cobra
cobra1.speed(0)  # velocidade instântanea
cobra1.penup()
cobra1.color("blue")
cobra1.shape("cobra.gif")
cobra1.shapesize(stretch_wid=18, stretch_len=3, outline=None)
cobra1.goto(300, 250)  # define coordenada da cobra 1
cobra1.dx = -2  # velocidade de movimentação
cobra1.dy = 0
cobra1.value = 1  # valor pra pontuação

# Criação do cone 1
cone_1 = turtle.Turtle('cone.gif')  # adiciona imagem do cone
cone_1.speed(0)
cone_1.penup()
cone_1.color("blue")
cone_1.shape("cone.gif")
cone_1.shapesize(stretch_wid=18, stretch_len=3, outline=None)
cone_1.goto(300, -250)  # define coordenada do cone 1
cone_1.dx = -2  # velocidade de movimentação
cone_1.dy = 0

# Criação da cobra 1
cobra2 = turtle.Turtle('cobra.gif')  # adiciona imagem da cobra
cobra2.speed(0)
cobra2.penup()
cobra2.color("blue")
cobra2.shape("cobra.gif")
cobra2.shapesize(stretch_wid=18, stretch_len=3, outline=None)
cobra2.goto(600, 300)  # define coordenada da cobra 2
cobra2.dx = -2  # velocidade de movimentação
cobra2.dy = 0
cobra2.value = 1  # valor pra pontuação

# Criação do cone 2
cone_2 = turtle.Turtle('cone.gif')  # adiciona imagem do cone
cone_2.speed(0)
cone_2.penup()
cone_2.color("blue")
cone_2.shape("cone.gif")
cone_2.shapesize(stretch_wid=18, stretch_len=3, outline=None)
cone_2.goto(600, -200)  # define coordenada do cone 2
cone_2.dx = -2  # velocidade de movimentação
cone_2.dy = 0

gravidade = -0.3

# movimentação personagem


def salto():
    cavalo.dy += 8

    if cavalo.dy > 8:
        cavalo.dy = 8


# escuta a função
cenario.listen()
cenario.onkeypress(salto, "space")


# pontuação do cavalo
cavalo.score = 0

while True:

    cenario.update()

    # Tempo de pausa (quanto maior mais demorado)
    time.sleep(0.02)

    # Gravidade faz efeito no cavalo
    cavalo.dy += gravidade

    # Mover cavalo
    y = cavalo.ycor()   # define y como coordenada atual do cavalo
    y += cavalo.dy      # calcula a coordenada do cavalo com a gravidade
    cavalo.sety(y)      # altera a coordenada atual pela coordenada calculada

    # Campo de força na borda de baixo
    if cavalo.ycor() < -390:
        cavalo.dy = 0
        cavalo.sety(-390)       # impede o cavalo de cair pra fora da tela

    # Mover cobra 1
    x = cobra1.xcor()
    x += cobra1.dx
    cobra1.setx(x)

    # Mover cone 1
    x = cone_1.xcor()
    x += cone_1.dx
    cone_1.setx(x)

    # Retorna obstáculos pro começo (cobra 1 e cone 1)
    if cobra1.xcor() < -350:
        # quando os obstáculos saem da tela eles voltam pra onde começaram o jogo
        cobra1.setx(350)
        cone_1.setx(350)
        cobra1.value = 1

    # Mover cobra 2
    x = cobra2.xcor()
    x += cobra2.dx
    cobra2.setx(x)

    # Mover cone 2
    x = cone_2.xcor()
    x += cone_2.dx
    cone_2.setx(x)

    # Retorna obstáculos pro começo (cobra 2 e cone 2)
    if cobra2.xcor() < -350:
        # quando os obstáculos saem da tela eles voltam pra onde começaram o jogo
        cobra2.setx(350)
        cone_2.setx(350)
        cobra2.value = 1

    # Colisão entre cavalo e cobra 1 / cone 1
    if (cavalo.xcor() + 10 > cobra1.xcor() - 30) and (cavalo.xcor() - 10 < cobra1.xcor() + 30):
        if (cavalo.ycor() + 10 > cobra1.ycor() - 150) or (cavalo.ycor() - 10 < cone_1.ycor() + 180):
            placar.clear()
            placar.write("Game Over", move=False, align="center",
                         font=("Arial", 16, "normal"))
            cenario.update()
            time.sleep(3)
            # Se o cavalo bater nos obstáculos o jogador perde seus pontos (limpa o placar)
            cavalo.score = 0
            # Move os obstáculos pra posição inicial
            cobra1.setx(300)
            cone_1.setx(300)
            cobra1.setx(600)
            cone_1.setx(600)
            # Move o jogador pra posição inicial
            cavalo.goto(-200, 0)
            cavalo.dy = 0

    # Atualiza o placar
    if cobra1.xcor() + 30 < cavalo.xcor() - 10:
        # soma a pontuação
        cavalo.score += cobra1.value
        cobra1.value = 0
        # limpa o placar
        placar.clear()
        placar.write(cavalo.score, move=False, align="center",
                     font=("Arial", 32, "normal"))

    # Colisão entre cavalo e cobra 2 / cone 2
    if (cavalo.xcor() + 10 > cobra2.xcor() - 30) and (cavalo.xcor() - 10 < cobra2.xcor() + 30):
        if (cavalo.ycor() + 10 > cobra2.ycor() - 150) or (cavalo.ycor() - 30 < cone_2.ycor() + 180):
            placar.clear()
            placar.write("Game Over", move=False, align="left",
                         font=("Arial", 16, "normal"))
            cenario.update()
            time.sleep(3)
            # Se o cavalo bater nos obstáculos o jogador perde seus pontos (limpa o placar)
            cavalo.score = 0
            # Move os obstáculos pra posição inicial
            cobra2.setx(300)
            cone_2.setx(300)
            cobra2.setx(600)
            cone_2.setx(600)
            # Move o jogador pra posição inical
            cavalo.goto(-200, 0)
            cavalo.dy = 0
            # Limpa placar
            placar.clear()

    # Atualizar o placar
    if cobra2.xcor() + 30 < cavalo.xcor() - 10:
        # soma a pontuação
        cavalo.score += cobra2.value
        cobra2.value = 0
        # limpa o placar
        placar.clear()
        placar.write(cavalo.score, move=False, align="left",
                     font=("Arial", 32, "normal"))

    # Se a pontuação for igual a 5 o fundo muda
    if (cavalo.score > 4):
        cenario.bgpic("fundo_noite.gif")
