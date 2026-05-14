n = int(input())

total = 0
sapos = 0
ratos = 0
coelhos = 0

i = 0
while i < n:
    linha = input().split()
    quantia = int(linha[0])
    tipo = linha[1]

    if tipo == "S":
        sapos = sapos + quantia
    elif tipo == "R":
        ratos = ratos + quantia
    elif tipo == "C":
        coelhos = coelhos + quantia

    total = total + quantia
    i = i + 1

perc_coelhos = (coelhos / total) * 100
perc_ratos = (ratos / total) * 100
perc_sapos = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")
