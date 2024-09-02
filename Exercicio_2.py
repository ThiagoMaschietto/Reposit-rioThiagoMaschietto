num = int(input("Digite o número para a verificação: "))
confirmador = False
indice = 0
valor1 = 0
valor2 = 1
valor_auxiliar = 0

while indice <= num:
    if num == 0:
        print("Pertence a sequencia!")
        confirmador = True
    
    valor_auxiliar = valor2
    valor2 += valor1
    valor1 = valor_auxiliar

    if num == valor2:
        print("Pertence a sequencia!")
        confirmador = True

    indice += 1

if not confirmador:
    print("Não pertence a Sequencia!")