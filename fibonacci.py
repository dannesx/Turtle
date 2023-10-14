import turtle

# Configurações do Turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.color("grey")

# Variáveis
fibonacci = []
n = int(input("Digite um valor maior que 1: "))

t.speed(0)

for i in range(n):
    if i < 2: 
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    for j in range(5):
        t.forward(fibonacci[i])
        t.left(90)
        
    t.forward(fibonacci[i])

t.penup()
t.goto(0,0)
t.setheading(0)
t.speed(6)
t.color("white")
t.pendown()

for x in fibonacci:     
    t.circle(x, 90)

turtle.mainloop()