ano = int(input("Digite um ano: "))
if ano % 400 == 0:
    print(ano, "é bissexto.")
else:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print(ano, "é bissexto.")
        else:
            print(ano, "não é bissexto.")
    else:
        print(ano, "não é bissexto.")
        
        
        
        
ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    bissexto = True
elif ano % 100 == 0:
    bissexto = False
elif ano % 4 == 0:
    bissexto = True
else:
    bissexto = False

if bissexto:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
