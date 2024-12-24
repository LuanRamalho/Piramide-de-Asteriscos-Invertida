# Solicitar o número de linhas ao usuário
print("Quantas linhas você deseja?")
no_of_rows = int(input())

print("Aqui está sua pirâmide invertida de asteriscos:")

for i in range(no_of_rows):
    # Imprimir espaços
    for j in range(i):
        print(" ", end="")
    
    # Imprimir asteriscos
    for j in range(2 * (no_of_rows - i) - 1):
        print("*", end="")
    
    print()  # Quebra de linha após cada linha

input()
