

cpfvalido = str(input("Digite seu CPF para verificar se está correto : "))
cpf = []


for n in cpfvalido:
      if n in "0123456789":
            valor= int(n)
            cpf.append(valor)
 

valor_1 = (10*cpf[0]+9*cpf[1]+8*cpf[2]+7*cpf[3]+6*cpf[4]+5*cpf[5]+4*cpf[6]+3*cpf[7]+2*cpf[8])%11

if (valor_1<2):
      digito_1 = 0
else: 
      digito_1 = 11-valor_1

valor_2 = (11*cpf[0]+10*cpf[1]+9*cpf[2]+8*cpf[3]+7*cpf[4]+6*cpf[5]+5*cpf[6]+4*cpf[7]+3*cpf[8]+2*cpf[9])%11

print(valor_2)

if (valor_2<2):
      digito_2 = 0
else: 
      digito_2 = 11-valor_2

if (cpf[-2] != digito_1 and cpf[-1] != digito_2):
      print("CPF não está correto!")
else:
      print("CPF está correto!")