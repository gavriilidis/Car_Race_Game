# World Hardest Game - Γαβριηλίδης Γαβριήλ
# ΣΘΕΤ-ΑΨΛ(Δ)
# 2η ΑΕ Μέρος 4
# Python 3.10
import turtle

# Δημιουργία παραθύρου
wn = turtle.Screen()
wn.bgcolor("light slate blue")
wn.setup(width=1200, height=600)
wn.title("World Hardest Game by Gavriil Gavriilidis")
wn.tracer(0)

# Η φωτογραφία στο κέντρο
wn.register_shape("field.gif")

# Το περίγραμμα του παιχνιδιού
board = turtle.Turtle()
board.speed(0)
board.penup()
board.pencolor("black")
board.pensize(3)
board.goto(-450, 150)
board.fillcolor("silver")
board.begin_fill()
board.pendown()
board.forward(150)
board.right(90)
board.forward(250)
board.left(90)
board.forward(50)
board.left(90)
board.forward(200)
board.right(90)
board.forward(450)
board.left(90)
board.forward(50)
board.right(90)
board.forward(250)
board.right(90)
board.forward(300)
board.right(90)
board.forward(150)
board.right(90)
board.forward(250)
board.left(90)
board.forward(50)
board.left(90)
board.forward(200)
board.right(90)
board.forward(450)
board.left(90)
board.forward(50)
board.right(90)
board.forward(250)
board.right(90)
board.forward(300)
board.end_fill()
board.hideturtle()
field = turtle.Turtle()
field.shape("field.gif")

# Ο παίκτης
player = turtle.Turtle()
player.speed(0)
player.color("black")
player.shape("square")
player.fillcolor("red")
player.shapesize(1.2)
player.penup()
player.goto(-400, 0)
player.direction = "stop"


# Οι μπάλες
ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.color("black")
ball_1.shape("circle")
ball_1.fillcolor("blue")
ball_1.shapesize(1.5)
ball_1.penup()
ball_1.setposition(0, 75)
ball_1.direction = "left"

ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.color("black")
ball_2.shape("circle")
ball_2.fillcolor("blue")
ball_2.shapesize(1.5)
ball_2.penup()
ball_2.setposition(0, 25)
ball_2.direction = "right"

ball_3 = turtle.Turtle()
ball_3.speed(0)
ball_3.color("black")
ball_3.shape("circle")
ball_3.fillcolor("blue")
ball_3.shapesize(1.5)
ball_3.penup()
ball_3.setposition(0, -25)
ball_3.direction = "left"

ball_4 = turtle.Turtle()
ball_4.speed(0)
ball_4.color("black")
ball_4.shape("circle")
ball_4.fillcolor("blue")
ball_4.shapesize(1.5)
ball_4.penup()
ball_4.setposition(0, -75)
ball_4.direction = "right"


# Οι μπάλες 1 & 3 ξεκινούν προς τα αριστερά και μετά δεξιά
def move_balls_1_3():
    if ball_1.direction == "left":
        ball_1.setx(ball_1.xcor() - 1)
    if ball_1.direction == "right":
        ball_1.setx(ball_1.xcor() + 1)
    if ball_1.xcor() < -235:
        ball_1.direction = "right"
    if ball_1.xcor() > 235:
        ball_1.direction = "left"

    if ball_3.direction == "left":
        ball_3.setx(ball_3.xcor() - 1)
    if ball_3.direction == "right":
        ball_3.setx(ball_3.xcor() + 1)
    if ball_3.xcor() < -235:
        ball_3.direction = "right"
    if ball_3.xcor() > 235:
        ball_3.direction = "left"


# Οι μπάλες 2 & 4 ξεκινούν προς τα δεξιά και μετά αριστερά
def move_balls_2_4():
    if ball_2.direction == "left":
        ball_2.setx(ball_2.xcor() - 1)
    if ball_2.direction == "right":
        ball_2.setx(ball_2.xcor() + 1)
    if ball_2.xcor() < -235:
        ball_2.direction = "right"
    if ball_2.xcor() > 235:
        ball_2.direction = "left"

    if ball_4.direction == "left":
        ball_4.setx(ball_4.xcor() - 1)
    if ball_4.direction == "right":
        ball_4.setx(ball_4.xcor() + 1)
    if ball_4.xcor() < -235:
        ball_4.direction = "right"
    if ball_4.xcor() > 235:
        ball_4.direction = "left"


# Ταχύτητα παίκτη
player_speed = 15


# Οι κινήσεις του παίκτη και οι περιορισμοί προς τα πάνω
def go_up():
    player.direction = "up"
    x = player.xcor()
    y = player.ycor()
    y += player_speed
    if y > 138:
        y = 138
    if -312 < x < -238 and y > -112:
        y = - 112
    if -250 < x < 212 and y > 88:
        y = 88
    player.sety(y)


# Οι κινήσεις του παίκτη και οι περιορισμοί προς τα κάτω
def go_down():
    player.direction = "down"
    x = player.xcor()
    y = player.ycor()
    y -= player_speed
    if y < -138:
        y = -138
    if -212 < x < 250 and y < -88:
        y = -88
    if 238 < x < 312 and y < 112:
        y = 112
    player.sety(y)


# Οι κινήσεις του παίκτη και οι περιορισμοί προς τα δεξιά
def go_right():
    player.direction = "right"
    y = player.ycor()
    x = player.xcor()
    x += player_speed
    if x > 438:
        x = 438
    if -312 < x < -238 and y > -112:
        x = -312
    if x > -212 and y < -88:
        x = -212
    if 312 > x > 238 and -100 < y < 112:
        x = 238
    player.setx(x)


# Οι κινήσεις του παίκτη και οι περιορισμοί προς τα αριστερά
def go_left():
    player.direction = "left"
    y = player.ycor()
    x = player.xcor()
    x -= player_speed
    if x < -438:
        x = -438
    if -312 < x < -238 and -100 < y < 100:
        x = -238
    if x < 212 and 88 < y < 150:
        x = 212
    if 312 > x > 238 and y < 112:
        x = 312
    player.setx(x)


# Τα κουμπιά
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")
wn.listen()


# Έλεγχος για σύγκρουση του παίκτη με τις μπάλες
def collision():
    if ball_1.distance(player) < 30:
        player.goto(-400, 0)
    if ball_2.distance(player) < 30:
        player.goto(-400, 0)
    if ball_3.distance(player) < 30:
        player.goto(-400, 0)
    if ball_4.distance(player) < 30:
        player.goto(-400, 0)


# Κύριο μέρος παιχνιδιού
while True:
    wn.update()
    move_balls_1_3()
    move_balls_2_4()
    collision()
    # Αν ο παίκτης φτάσει στη δεξιά περιοχή εμφανίζεται το μήνυμα ότι κέρδισε
    if player.xcor() > 212 and player.ycor() > 112:
        turtle.penup()
        turtle.goto(0, 200)
        turtle.write("You Win", align="center", font=("Ariel", 40, "bold"))
        turtle.hideturtle()
    wn.update()
