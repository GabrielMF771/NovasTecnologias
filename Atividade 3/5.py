L1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
L2 = {2, 4, 6, 8, 10, 11}

intercesao = L1 & L2
print(f"Valores comuns: {intercesao}")

somente_l1 = L1 - L2
print(f"Apenas na L1: {somente_l1}")

somente_l2 = L2 - L1
print(f"Apenas na L2: {somente_l2}")

uniao = L1 | L2
print(f"União de todos os elementos (sem repetir): {uniao}")

so_exclusivos = L1 ^ L2
print(f"Elementos que não se repetem em ambas: {so_exclusivos}")