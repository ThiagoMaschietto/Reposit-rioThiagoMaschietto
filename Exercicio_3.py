FATURAMENTO_MENSAL = {
    "01": "R$ 0.00", "02": "R$ 20000.00", "03" : "R$ 15000.00",
    "04": "R$ 10000.00", "05": "R$ 71000.50", "06" : "R$ 9000.76",
    "07": "R$ 0.00", "08": "R$ 0.00", "09" : "R$ 32040.00",
    "10": "R$ 34560.00", "11": "R$ 40000.00", "12" : "R$ 50000.00",
    "13": "R$ 90000.00", "14": "R$ 0.00", "15" : "R$ 0.00",
    "16": "R$ 23400.00", "17": "R$ 12300.00", "18" : "R$ 18900.00",
    "19": "R$ 8000.00", "20": "R$ 30000.00", "21" : "R$ 0.00",
    "22": "R$ 0.00", "23": "R$ 21000.00", "24" : "R$ 53400.00",
    "25": "R$ 23000.00", "26": "R$ 32000.00", "27" : "R$ 53000.00",
    "28": "R$ 0.00", "29": "R$ 0.00", "30" : "R$ 67000.00",
}

def media():
    divisor_da_media = 0
    soma = 0

    for indice in FATURAMENTO_MENSAL.values():
        indice = indice.replace("R$ ","")
        
        if float(indice) != 0.00:
            soma += float(indice)
            divisor_da_media += 1
        
    return soma/divisor_da_media

numero_de_dias_sup = 0
minimo = 0.00
maximo = 0.00
media = media()

for indice in FATURAMENTO_MENSAL.values():
    indice = indice.replace("R$ ","")

    if float(indice) > media:
        numero_de_dias_sup += 1


    if minimo == 0.00:
        minimo = float(indice)

    if float(indice) > maximo:
        maximo = float(indice)
    
    if float(indice) < minimo and float(indice) != 0.00:
        minimo = float(indice)



print(f"Valor Maximo:{maximo}, Valor Minimo:{minimo}, Numero De Dias Valor superior a media:{numero_de_dias_sup}.")

