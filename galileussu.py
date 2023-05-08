somaDosQuadrados = 0
x= 1
while x <= 100:
    somaDosQuadrados = somaDosQuadrados + x**2
    x = x+1

quadradoDaSoma = 0
y = 1

while y <= 100:
  quadradoDaSoma = quadradoDaSoma + y
  y = y + 1

quadradoDaSoma = quadradoDaSoma**2

print("A diferença da soma dos quadrados dos primeiros cem números naturais pelo o quadrado da soma dos primeiros cem números naturais é: ", quadradoDaSoma - somaDosQuadrados)

