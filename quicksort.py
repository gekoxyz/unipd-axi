import random

# Quick-Sort 
# Algoritmo che ordina una sequenza S di n oggetti usando divide and conquer
# - caso base: S ha meno di 2 elementi, termina
# - divisione: scegli un elemento x in S (pivot) ed estrai tutti gli elementi da S,
#              inserendoli in 3 sequenze, che risultano essere una partizione di S
#              - L contiene gli elementi minori di x
#              - E contiene gli elementi uguali a x (solo x se gli elementi di S sono tutti distinti)
#              - G contiene gli elementi maggiori di x
# - ricorsione: ordina ricorsivamente L e G (E e' già ordinata)
# - conquista: re-inserisci gli elementi in S (che era rimasta vuota), prima quelli di L, poi quelli di E, infine quelli di G
def quicksort(arr):
    if len(arr) <= 1: return arr

    pivot = arr[random.randint(0,len(arr)- 1)]

    L = []
    E = []
    G = []

    for el in arr:
        if el < pivot:
            L.append(el)
        elif el > pivot:
            G.append(el)
        else:
            E.append(el)

    return quicksort(L) + E + quicksort(G)

# Set the length of the list and the range of the random numbers
length = 10 
min_val = 1
max_val = 100

# Generate the list of random integers
random_numbers = [random.randint(min_val, max_val) for _ in range(length)]

print(random_numbers)

sorted = quicksort(random_numbers)

print(sorted)

