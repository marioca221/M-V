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
        <style rel="styleshet">
            table, tr, td{
                border: 1px solid black;
            }
            .aprovado{
                background: green;
                color: wheat;
            }
            .reprovado{
                background: red;
                color: wheat
            }
        </style>
    </head>
    <body>
        <h1>Notas de cada aluno</h1>
        <hr>
      ''' 
        )
 
        for c,v in DS.items():
            file.write(
            f'''
            <table>
            <caption style="font-size: xx-large;">{c}</caption>
            <tr>
                <th></th>
                <th>1° Bimestre</th>
                <th>2° Bimestre</th>
                <th>3° Bimestre</th>
                <th>4° Bimestre</th>
                <th>Media</th>
            </tr>
            '''
            )
            n = 0
            n2 = 0
            confirmacao = 0
            for m in v:
                n = 0
                file.write(f'<tr>')
                file.write(f'<td>{materias[n2]}</td>')
                for notis in v[materias[n2]]:
                    print(n, notis)
                    if(n == 4):
                        if (notis<6):
                            file.write(f"<td class = 'reprovado'>{str(notis)}</td>")
                        else:
                            file.write(f"<td class = 'aprovado'>{str(notis)}</td>")
                    else:
                        file.write(f"<td>{str(notis)}</td>")
                    n+=1
                n2+=1
                file.write(f'</tr>')