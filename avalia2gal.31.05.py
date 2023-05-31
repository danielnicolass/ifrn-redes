import matplotlib.pyplot as plt
import random
x = 0
y = 0
xn = 0
yn = 0
passo = 5
plt.axis((-30, 70, -40, 60))
for _ in range(300):
    mov = random.randint(1,4)
    distancia += passo
    if mov == 1 and y < 60:
        yn = y + 1
        cor= "r."
        distancia += passo
    elif mov == 2 and y > -40:
        yn = y - 1
        cor = "g."
        distancia += passo
    elif mov == 3 and x < 70:
        xn = x + 1
        cor = "b."
        distancia += passo
    elif x > -30:
        xn = x - 1
        cor = "y."
        distancia += passo
    else:
        distancia -= passo

    plt.plot((x, xn), (y, yn), cor)

plt.show()
print("Posição final: (", x, ",", y, ")")
print("Distancia pecorrida: ", distancia)
