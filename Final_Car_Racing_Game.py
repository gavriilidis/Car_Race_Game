# Car Racing Game από τον Γαβριήλ Γαβριηλίδη
# ΣΘΕΤ-ΑΨΛ(Δ)
# 2η ΑΕ μέρος 5 (προαιρετικό)
# Python 3.10

import turtle
import random
import winsound


# Αν θέλουμε να παίξουμε ξανά στο τέλος υπάρχει επιλογή y/n. Αν η επιλογή είναι y, τρέχει run_game() και αρχίζει πάλι.
def run_game():
    # Παράθυρο παιχνιδιού
    wn = turtle.Screen()
    wn.setup(width=700, height=720)
    wn.bgcolor("black")
    wn.title("Car Racing by Gavriil Gavriilidis")
    wn.tracer(False)

    # Εικόνες αυτοκινήτων
    wn.register_shape("player.gif")
    wn.register_shape("car_1.gif")
    wn.register_shape("car_2.gif")
    wn.register_shape("car_3.gif")
    wn.register_shape("car_4.gif")
    wn.register_shape("car_5.gif")

    # Όρια αυτοκινητόδρομου
    red_lines = turtle.Turtle()
    red_lines.speed(0)
    red_lines.color("red")
    red_lines.penup()
    red_lines.left(90)
    red_lines.goto(-250, -360)
    red_lines.pensize(20)
    red_lines.pendown()
    red_lines.forward(720)
    red_lines.penup()
    red_lines.goto(250, -360)
    red_lines.pendown()
    red_lines.forward(720)
    red_lines.hideturtle()

    # Λωρίδες δρόμου
    white_lines = turtle.Turtle()
    white_lines.speed(0)
    white_lines.color("grey")
    white_lines.penup()
    white_lines.left(90)
    x = -150
    for i in range(4):
        white_lines.goto(x, -320)
        white_lines.pensize(6)
        x += 100
        for j in range(5):
            white_lines.pendown()
            white_lines.forward(80)
            white_lines.penup()
            white_lines.forward(80)
    white_lines.hideturtle()

    # Πίνακας σκορ
    score = 0
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-340, 300)
    score_string = "Score:\n{}".format(score)
    score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))
    score_pen.hideturtle()

    # Ζωές
    lives = 3
    lives_pen = turtle.Turtle()
    lives_pen.speed(0)
    lives_pen.color("white")
    lives_pen.penup()
    lives_pen.setposition(270, 300)
    lives_string = "Lives:\n{}".format(lives)
    lives_pen.write(lives_string, False, align="left", font=("Arial", 14, "bold"))
    lives_pen.hideturtle()

    # Παίκτης
    player = turtle.Turtle()
    player.speed(0)
    player.hideturtle()
    player.penup()
    player.color("red")
    player.shape("player.gif")
    player.setheading(90)
    player.turtlesize(2)
    player.goto(0, -280)
    player.showturtle()
    player_speed = 15

    # Κίνηση παίκτη δεξιά αριστερά
    def go_right():
        x = player.xcor()
        x += player_speed
        if x > 200:
            x = 200
        player.setx(x)

    def go_left():
        x = player.xcor()
        x -= player_speed
        if x < -200:
            x = -200
        player.setx(x)

    # Πλήκτρα
    turtle.listen()
    turtle.onkeypress(go_right, "Right")
    turtle.onkeypress(go_left, "Left")

    # Αυτοκίνητο 1
    car_1 = turtle.Turtle()
    car_1.speed(0)
    car_1.hideturtle()
    car_1.penup()
    car_1.color("yellow")
    car_1.shape("car_1.gif")
    car_1.setheading(90)
    car_1.turtlesize(2)
    car_1.goto(0, 400)
    car_1.showturtle()

    # Αυτοκίνητο 2
    car_2 = turtle.Turtle()
    car_2.hideturtle()
    car_2.penup()
    car_2.color("green")
    car_2.shape("car_2.gif")
    car_2.setheading(90)
    car_2.turtlesize(2)
    car_2.goto(-100, 400)
    car_2.showturtle()

    # Αυτοκίνητο 3
    car_3 = turtle.Turtle()
    car_3.hideturtle()
    car_3.penup()
    car_3.color("light blue")
    car_3.shape("car_3.gif")
    car_3.setheading(90)
    car_3.turtlesize(2)
    car_3.goto(-200, 400)
    car_3.showturtle()
    winsound.PlaySound("car_engine.wav", winsound.SND_ASYNC)

    # Αυτοκίνητο 4
    car_4 = turtle.Turtle()
    car_4.hideturtle()
    car_4.penup()
    car_4.color("white")
    car_4.shape("car_4.gif")
    car_4.setheading(90)
    car_4.turtlesize(2)
    car_4.goto(200, 400)
    car_4.showturtle()

    # Αυτοκίνητο 5
    car_5 = turtle.Turtle()
    car_5.hideturtle()
    car_5.penup()
    car_5.color("purple")
    car_5.shape("car_5.gif")
    car_5.setheading(90)
    car_5.turtlesize(2)
    car_5.goto(100, 400)
    car_5.showturtle()

    # Κίνηση Αυτοκινήτου 1 προς τα κάτω. Αν κατέβει κάτω από τον παίκτη εκτελεί την τυχαία επανεκκίνηση
    def move_car_1():
        car_1.sety(car_1.ycor() - 0.15)
        if car_1.ycor() < -350:
            car_1_loop()

    # Στέλνει το Αυτοκίνητο 1 επάνω σε τυχαία λωρίδα κυκλοφορίας
    def car_1_loop():
        car_1.hideturtle()
        a = random.randint(1, 5)
        if a == 1:
            car_1.goto(-200, 400)
        elif a == 2:
            car_1.goto(-100, 400)
        elif a == 3:
            car_1.goto(0, 400)
        elif a == 4:
            car_1.goto(100, 400)
        else:
            car_1.goto(200, 400)
        car_1.showturtle()

    # Κίνηση Αυτοκινήτου 2 προς τα κάτω. Αν κατέβει κάτω από τον παίκτη εκτελεί την τυχαία επανεκκίνηση
    def move_car_2():
        car_2.sety(car_2.ycor() - 0.2)
        if car_2.ycor() < -350:
            car_2_loop()

    # Στέλνει το Αυτοκίνητο 2 επάνω σε τυχαία λωρίδα κυκλοφορίας
    def car_2_loop():
        car_2.hideturtle()
        a = random.randint(1, 5)
        if a == 1:
            car_2.goto(-200, 400)
        elif a == 2:
            car_2.goto(-100, 400)
        elif a == 3:
            car_2.goto(0, 400)
        elif a == 4:
            car_2.goto(100, 400)
        else:
            car_2.goto(200, 400)
        car_2.showturtle()

    # Κίνηση Αυτοκινήτου 3 προς τα κάτω. Αν κατέβει κάτω από τον παίκτη εκτελεί την τυχαία επανεκκίνηση
    def move_car_3():
        car_3.sety(car_3.ycor() - 0.3)
        if car_3.ycor() < -350:
            car_3_loop()

    # Στέλνει το Αυτοκίνητο 3 επάνω σε τυχαία λωρίδα κυκλοφορίας
    def car_3_loop():
        car_3.hideturtle()
        a = random.randint(1, 5)
        if a == 1:
            car_3.goto(-200, 400)
        elif a == 2:
            car_3.goto(-100, 400)
        elif a == 3:
            car_3.goto(0, 400)
        elif a == 4:
            car_3.goto(100, 400)
        else:
            car_3.goto(200, 400)
        car_3.showturtle()
        # Έβαλα εδώ τον ήχο της μηχανής γιατί μετά από δοκιμές
        # ήταν η καλύτερη επιλογή σε συνδυασμό με τον ήχο τρακαρίσματος
        winsound.PlaySound("car_engine.wav", winsound.SND_ASYNC)

    # Κίνηση Αυτοκινήτου 4 προς τα κάτω. Αν κατέβει κάτω από τον παίκτη εκτελεί την τυχαία επανεκκίνηση
    def move_car_4():
        car_4.sety(car_4.ycor() - 0.4)
        if car_4.ycor() < -350:
            car_4_loop()

    # Στέλνει το Αυτοκίνητο 4 επάνω σε τυχαία λωρίδα κυκλοφορίας
    def car_4_loop():
        car_4.hideturtle()
        a = random.randint(1, 5)
        if a == 1:
            car_4.goto(-200, 400)
        elif a == 2:
            car_4.goto(-100, 400)
        elif a == 3:
            car_4.goto(0, 400)
        elif a == 4:
            car_4.goto(100, 400)
        else:
            car_4.goto(200, 400)
        car_4.showturtle()

    # Κίνηση Αυτοκινήτου 5 προς τα κάτω. Αν κατέβει κάτω από τον παίκτη εκτελεί την τυχαία επανεκκίνηση
    def move_car_5():
        car_5.sety(car_5.ycor() - 0.5)
        if car_5.ycor() < -350:
            car_5_loop()

    # Στέλνει το Αυτοκίνητο 5 επάνω σε τυχαία λωρίδα κυκλοφορίας
    def car_5_loop():
        car_5.hideturtle()
        a = random.randint(1, 5)
        if a == 1:
            car_5.goto(-200, 400)
        elif a == 2:
            car_5.goto(-100, 400)
        elif a == 3:
            car_5.goto(0, 400)
        elif a == 4:
            car_5.goto(100, 400)
        else:
            car_5.goto(200, 400)
        car_5.showturtle()

    def collision():
        if car_1.distance(player) < 50:
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)
            car_1_loop()
            return True
        if car_2.distance(player) < 50:
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)
            car_2_loop()
            return True
        if car_3.distance(player) < 50:
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)
            car_3_loop()
            return True
        if car_4.distance(player) < 50:
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)
            car_4_loop()
            return True
        if car_5.distance(player) < 50:
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)
            car_5_loop()
            return True

    # Κύριο μέρος παιχνιδιού
    while True:
        wn.update()

        # Αν δεν έχουν τελειώσει οι ζωές κινούνται τα αυτοκίνητα
        if lives != 0:
            move_car_1()
            move_car_2()
            move_car_3()
            move_car_4()
            move_car_5()

            # Αν υπάρχει επαφή χάνει ο παίκτης μια ζωή.
            if collision():
                lives -= 1
                lives_string = "Lives:\n{}".format(lives)
                lives_pen.clear()
                lives_pen.write(lives_string, False, align="left", font=("Arial", 14, "bold"))

            # Κάθε αυτοκίνητο που αποφεύγουμε μας δίνει πόντους ανάλογα με την ταχύτητα τους. (10, 20, 30, 40, 50)
            if car_1.ycor() < -349.9:
                score += 10
                score_string = "Score:\n{}".format(score)
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))
            if car_2.ycor() < -349.9:
                score += 20
                score_string = "Score:\n{}".format(score)
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))
            if car_3.ycor() < -349.7:
                score += 30
                score_string = "Score:\n{}".format(score)
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))
            if car_4.ycor() < -349.9:
                score += 40
                score_string = "Score:\n{}".format(score)
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))
            if car_5.ycor() < -349.9:
                score += 50
                score_string = "Score:\n{}".format(score)
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))

        # Αν έχουν τελειώσει οι ζωές τελειώνει το παιχνίδι και παίζει ήχος
        else:
            game_over = turtle.Turtle()
            game_over.hideturtle()
            game_over.color("white")
            game_over.shape("circle")
            game_over.speed(0)
            game_over.penup()
            game_over.goto(0, 150)
            game_over.write("Game Over!!!", align="center", font=("Ariel", 40, "bold"))
            winsound.PlaySound("game_over.wav", winsound.SND_ASYNC)

            # Ανοίγει παράθυρο και επιλέγουμε αν θέλουμε να παίξουμε ξανά ή όχι
            restart = wn.textinput("Θες να παίξεις ξανά;", "(y/n)").lower()
            while restart != "y" or restart != "n":
                # συνεχίζει να ρωτάει αν δεν έχει δώσει ο παίκτης μια από τις δύο επιλογές
                restart = wn.textinput("Θες να παίξεις ξανά;", "(y/n)").lower()
                if restart == "y":
                    # Αν ο παίκτης επιλέξει να ξαναπαίξει, καθαρίζει το παράθυρο και ξεκινάει απο την αρχή
                    wn.clearscreen()
                    run_game()
                if restart == "n":
                    # Αν ο παίκτης επιλέξει να σταματήσει το παράθυρο κλείνει στο πρώτο click
                    turtle.Screen().exitonclick()


run_game()