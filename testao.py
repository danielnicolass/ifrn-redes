soma = 0
x = 1
while x < 1000:
    ndivx = 0
    k=1
    while k<=x:
        if x%k==0:
            ndivx=ndivx+1
        k=k+1
    if ndivx==2:
        soma=soma+x
    x=x+1

print(soma)
