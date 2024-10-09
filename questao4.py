'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''

# faturamento por estado:
fat_men_sp = 67836.43
fat_men_rj = 36678.66
fat_men_mg = 29229.88
fat_men_es = 27165.48
fat_men_ou = 19849.53

# fat total
fat_total = fat_men_sp + fat_men_rj + fat_men_mg + fat_men_es + fat_men_ou

# porcentagem de cada estado
pct_sp = fat_men_sp / fat_total * 100
pct_rj = fat_men_rj / fat_total * 100
pct_mg = fat_men_mg / fat_total * 100
pct_es = fat_men_es / fat_total * 100
pct_ou = fat_men_ou / fat_total * 100
pct_total = pct_sp + pct_rj + pct_mg + pct_es + pct_ou

# resposta
print(f"Porcentagem de SP: {pct_sp}%")
print(f"Porcentagem de RJ: {pct_rj}%")
print(f"Porcentagem de MG: {pct_mg}%")
print(f"Porcentagem de ES: {pct_es}%")
print(f"Porcentagem de Outros: {pct_ou}%")
print(f"\nSomando todas as partes: {pct_sp}% + {pct_rj}% + {pct_mg}% + {pct_es}% + {pct_ou}% = {pct_total}%")