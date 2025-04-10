import json
import os.path
DS = {
}
if os.path.isfile('aluno.txt') == False:
    print("Não existe")
else:
    with open('aluno.txt', 'r',  encoding="utf-8") as file:
        DS = json.load(file)
   

    materias = ["Matemática", "Português", "História", "Filosofia"]
    quantidade = int(input("Quantos alunos quer cadastrar? \n"))
    for n in range(0,quantidade):
        while True:
            nome = input(f"Qual o nome do {n+1}° aluno? \n")
            if not(DS.get(nome)):
                break
            else:
                print("Usuário já existe. Informe outro nome... \n")
        print(DS.get(nome))
        DS[nome] = dict()
        for n1 in range(0,4):
            print(f"Estamos na matéria {materias[n1]}")
            lista = []
            nota2 = 0
            nota = -1
            for n in range(1,5):
                nota = -1
                while(nota<0 or nota>10):
                    nota = float(input(f"Digite a {n}° nota: \n"))
                nota2 = nota2+nota
                lista.append(nota)
            media = nota2/4
            lista.append(media)
            
            DS[nome][materias[n1]] = lista



    r = json.dumps(DS, ensure_ascii=False)
    with open('aluno.txt','w', encoding="utf-8") as arquivo:
        arquivo.write(r)

    with open("alunos_3ds.html",'w', encoding="utf-8") as file:
        file.write(
        '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notas 3°DS</title>
    </head>
    <body>
        <h1>Notas de cada aluno</h1>
        <hr>
      '''  
    )
        
        for c,v in DS.items():
            n = 0
            file.write("<h1>")
            file.write(c)
            file.write("</h1><br>")
            print(c, "c")
            print(v, "c")
            for m in v:
                file.write(m)
                print(m, "m")
                file.write(": <br>")
                n2 = 0
                for notis in v[materias[n]]:
                    print(notis, "notis")
                    print(v[materias[n]], "v[materias[n]]")
                    if (n2==4):
                        file.write("Média - ")
                    else:
                        file.write(f"{n2+1}° Bimestre - ")
                    file.write(str(notis))
                    file.write("<br>")
                    n2+=1
                file.write("<br>")
            n+=1