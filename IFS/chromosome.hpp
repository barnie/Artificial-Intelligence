#ifndef __CHROMOSOME__HPP__
#define __CHROMOSOME__HPP__

#include <array>
#include <iostream>
#include <cstdlib>
#include <ctime>

#define CHROMOSOME_SIZE  9

template <class T>
class Chromosome {
public:
    std::array<T, CHROMOSOME_SIZE>  chromosome;
    Chromosome();
    Chromosome(std::array<T, CHROMOSOME_SIZE> chromosome);
    void set_chromosome(std::array<T,CHROMOSOME_SIZE> _array);
    int get_size();
    void to_string();
};

template <class T>
Chromosome<T>::Chromosome() {
}

template <class T>
Chromosome<T>::Chromosome(std::array<T, CHROMOSOME_SIZE> chromosome) {
    this->chromosome = chromosome;
}

template <class T>
void Chromosome<T>::set_chromosome(std::array<T,CHROMOSOME_SIZE> _array) {
    this->chromosome = _array;
}

template <class T>
int Chromosome<T>::get_size() {
    return chromosome.size();
}

template <class T>
void Chromosome<T>::to_string(){
    for (int i = 0; i < CHROMOSOME_SIZE; i++){
        std::cout << chromosome[i] << " ";
    }
    std::cout << "\n";
}

template <class T>
Chromosome<T> crossover(Chromosome<T> p1, Chromosome<T> p2){
    srand( time( NULL ) );
    int index = rand() % CHROMOSOME_SIZE;
    Chromosome <T> e;
    std::copy(p1.chromosome.data(), p1.chromosome.data() + index, e.chromosome.data());
    std::copy(p2.chromosome.data() + index, p2.chromosome.data() + CHROMOSOME_SIZE, e.chromosome.data() + index);
    return e;
}

template<class T>
Chromosome<T> arithmetic_crossover(Chromosome<T> p1, Chromosome<T> p2){
    Chromosome <T> c1;
    Chromosome <T> c2;
    double a = 0.5;
    for (int i = 0; i < CHROMOSOME_SIZE; i++) {
        c1.chromosome[i] = p1.chromosome[i] * (1.0 - a) + p2.chromosome[i] * a;
        c2.chromosome[i] = p1.chromosome[i] * a + p2.chromosome[i] * (1.0 - a);
    }
    return c1;
}

#endif
