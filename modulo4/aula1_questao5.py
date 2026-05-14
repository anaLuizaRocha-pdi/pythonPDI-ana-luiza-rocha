n = int(input("Quantidade de respondentes: "))

soma = 0
i = 0

while i < n:
    idade = int(input("Digite a idade: "))
    soma = soma + idade
    i = i + 1

media = soma / n
print("Média das idades:", media)
