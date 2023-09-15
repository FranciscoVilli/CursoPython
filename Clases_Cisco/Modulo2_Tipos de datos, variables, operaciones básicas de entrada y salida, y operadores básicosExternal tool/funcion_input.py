# La función input() es capaz de leer datos que fueron introducidos 
# por el usuario y pasar esos datos al programa en ejecución.

print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")



from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()