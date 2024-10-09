'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
façaum programa,na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

# chamo lib json para ler dados do json de exemplo e sys para logica de valor minimo
import json
import sys

# leio arquivo json
with open ("./files/dados.json", "r") as file:
    arquivo = json.load(file)

# crio vetor
faturamento_dias = []

# verifico dias que nao tiveram faturamento zero
for indice in arquivo:
    if (indice["valor"] > 0):
        faturamento_dias.append(indice["valor"])
    else:
        continue

# fazer a media do mes
faturamento_total = 0
qtdd_dias = len(faturamento_dias)

for faturamento_diario in faturamento_dias:
    faturamento_total += faturamento_diario

media_mensal = faturamento_total / qtdd_dias

# verificar quantos dias passaram do faturamento mensal
dias_sup = 0

for faturamento_diario in faturamento_dias:
    if faturamento_diario > media_mensal:
        dias_sup += 1
    else:
        continue

# pegar maior e menor faturamento diario sem usar o max() e min()
vmax, vmin = 0, sys.float_info.max

for faturamento_diario in faturamento_dias:

    if faturamento_diario > vmax:
        vmax = faturamento_diario
    elif faturamento_diario < vmin:
        vmin = faturamento_diario

# resposta
print(f"Dia com maior faturamento: {round(vmax, 2)}\nDia com menor faturamento: {round(vmin, 2)}\nQuantidade de dias acima do faturamento médio: {dias_sup}")
