#include <iostream>
#include <random>
#include <chrono>

/*
Quick-Sort 
 Algoritmo che ordina una sequenza S di n oggetti usando divide and conquer
 - caso base: S ha meno di 2 elementi, termina
 - divisione: scegli un elemento x in S (pivot) ed estrai tutti gli elementi da S,
    inserendoli in 3 sequenze, che risultano essere una partizione di S
    - L contiene gli elementi minori di x
    - E contiene gli elementi uguali a x (solo x se gli elementi di S sono tutti distinti)
    - G contiene gli elementi maggiori di x
 - ricorsione: ordina ricorsivamente L e G (E e' già ordinata)
 - conquista: re-inserisci gli elementi in S (che era rimasta vuota), prima quelli di L, poi quelli di E, infine quelli di G
*/

int main() {
    constexpr int ARRAY_SIZE = 10;
    int myArray[ARRAY_SIZE];
    // create a random device engine
    auto rd = std::random_device();
    // seed the engine with system time
    auto seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::seed_seq ss{seed};
    // setup a mersenne twister engine
    std::mt19937 gen(ss);
    // define a normal distribution over the interval [-100, 100]
    std::uniform_real_distribution<> dis(-100, 100);
    // generate random numbers and fill the array
    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        myArray[i] = static_cast<int>(dis(gen));
    }

    // TODO: EDIT ME

        // Print the resulting array
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        std::cout << myArray[i] << ", ";
    }
    std::cout << "\n";

    return 0;

    
}

