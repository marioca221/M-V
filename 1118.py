nota1 = 222
nota2 = -13
resposta = 123141
contador = 0
notas=[]
while True:
    while contador<2:
        nota = float(input())
        if(nota<0 or nota>10):
            print("nota invalida")
        else:
            notas.append(nota)
            contador+=1

    print(f'media = {sum(notas)/len(notas):2f}')
    print("novo calculo (1-sim 2-nao)")
    resposta = int(input())
    while str(resposta) not in "12":
        print("novo calculo (1-sim 2-nao)")
        resposta = int(input())
    if (resposta==1):
        notas = []
        contador = 0
    else:
        break
        


