import random as rd

x = rd.randint(0,1000)
y = rd.randint(0,1000)
z = rd.randint(0,1000)

resultado = (x+y)+z

rd.seed(0)

x = rd.random() 
y = rd.random()
z = rd.random()

resultado2=x+(y+z)

print(resultado2)
