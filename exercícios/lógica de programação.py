# dois copos: 3ml e 5ml faça um dos copos ter 2 ml

#copo1 = 5
#copo2= 3
#print(copo1-copo2, 'ml')
#2 escreva um program que retorne o valor hora com base no salário
#mensal e horas trabalhadas por mês


def hora_sal():

    sal_mensal = int(input('qual o salario mensal? '))
    horas_trabalhadas = int(input('quantas horas trabalhadas por dia? '))
    dias = int(input('quantos dias você trabalhou? '))
    horas_mes = horas_trabalhadas*dias
    sal_hora = sal_mensal/horas_mes

    

    print('R$:', sal_hora)

hora_sal()