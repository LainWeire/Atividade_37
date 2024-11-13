# Ler um vetor com 20 idades e exibir a maior e menor.

n = [int(input("Digite uma idade:   ")) for item in range(7)]
print(f"A maior idade é:    ", max(n))
print(f"A menor idade é:    ", min(n))
