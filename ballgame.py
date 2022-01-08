import turtle, time, random

speed = 0.135
score = 0
size = 1
size2 = 1.3

window = turtle.Screen()
window.title("FEED GAME")
window.bgcolor("lightyellow")
window.setup(width=700, height=700)
window.tracer(0)

head = turtle.Turtle(shape="circle")
head.speed(0)
head.shapesize(size)
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle(shape="turtle")
food.shapesize(size2)
food.speed(0)
food.color("green")
food.penup()
food.goto(0, 0)
food.shapesize(0.8, 0.8)

poison = turtle.Turtle(shape="turtle")
poison.shapesize(size2)
poison.speed(0)
poison.color("red")
poison.penup()
poison.goto(250, -100 )
poison.shapesize(0.9, 0.9)

poison2 = turtle.Turtle(shape="turtle")
poison2.shapesize(size2)
poison2.speed(0)
poison2.color("red")
poison2.penup()
poison2.goto(250, -100 )
poison2.shapesize(0.9, 0.9)

write = turtle.Turtle()
write.speed(0)
write.color("red")
write.penup()
write.goto(-260, 315)
write.hideturtle()
write.write("Score:{}".format(score), align="center", font=("Courier", 24, "normal"))

write2 = turtle.Turtle()
write2.speed(0)
write2.color("purple")
write2.penup()
write2.goto(150, 315)
write2.hideturtle()
write2.write("Speed:{}".format(speed), align="center", font=("Courier", 24, "normal"))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

while True:
    window.update()
    move()
    time.sleep(speed)
    
    if head.distance(food) < 20:
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        xx = random.randint(-350, 350)
        yy = random.randint(-350, 350)
        xxx = random.randint(-350, 350)
        yyy = random.randint(-350, 350)
        food.goto(x, y)
        poison.goto(xx,yy)
        poison2.goto(xxx,yyy)
        speed -= 0.0016
        time.sleep(speed)
        score += 10
        size += 0.19
        size2 += 0.09
        food.shapesize(size2)
        poison.shapesize(size2)
        poison2.shapesize(size2)
        head.shapesize(size)
        write.clear()
        write.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))   
        write2.clear()
        write2.write("Speed:{}".format(speed), align="center", font=("Courier", 24, "normal"))
    
    elif head.xcor() > 350 or head.xcor() < -350 or head.ycor() < -350 or head.ycor() > 350 or head.distance(poison) < 20 or head.distance(poison2) < 20:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        write.clear()
        score = 0
        write.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        size = 1
        size2 = 1.8       
        head.shapesize(size)
        food.shapesize(size2)
        poison.shapesize(size2)
        poison2.shapesize(size2)   
        speed = 0.135
        write2.clear()
        write2.write("Speed:{}".format(speed), align="center", font=("Courier", 24, "normal"))
    else:
        pass
