string_escolhida = "Paçoca"
string_trocada = ""
indice = len(string_escolhida) - 1

while indice >= 0:
    string_trocada += string_escolhida[indice]
    indice -= 1

print(string_trocada)