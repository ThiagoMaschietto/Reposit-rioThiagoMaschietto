SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

total = SP + RJ + MG + ES + OUTROS

percentual_sp = (100 * SP) / total

print(f"Percentual SP: {(100 * SP) / total:.2f}%")
print(f"Percentual Rj: {(100 * RJ) / total:.2f}%")
print(f"Percentual MG: {(100 * MG) / total:.2f}%")
print(f"Percentual ES: {(100 * ES) / total:.2f}%")
print(f"Percentual OUTROS: {(100 * OUTROS) / total:.2f}%")