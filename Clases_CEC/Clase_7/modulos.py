#Manera de utilizar los modulos de forma general

import math 
print(math.sin(math.pi/2))

#Manera de utilizar los modulos de forma mas especifica
from math import sin,pi
print(sin(pi/2))



pi = 22/7


#Manera de importar todo de forma especifica
from math import *      #Es bueno usar cuando no se sabe que usar
print(sin(pi/2))



#Uso de alias
import math as m       #al math se lo utiliza con m
print(m.sin(m.pi/2))



from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()