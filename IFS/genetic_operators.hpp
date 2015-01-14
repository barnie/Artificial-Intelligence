#ifndef GENETIC_OPERATORS_HPP
#define GENETIC_OPERATORS_HPP

#include <iostream>
#include "chromosome.hpp"
#include "string.h"

template < class T >
Chromosome<T> crossover(Chromosome<T> p1, Chromosome<T> p2){
    if (p1.get_size() != p2.get_size()){
        throw "Chromosome length is different!!\n";
    }
    srand( time( NULL ) );
    int cross = std::rand() % p1.get_size();
    Chromosome<T> _new(p1.get_size());
    T * tmp = new T [p1.get_size()];
    std::copy(p1.get_chromosome(), p1.get_chromosome() + cross, tmp);
    std::copy(p2.get_chromosome() + cross, p2.get_chromosome() + p2.get_size(), tmp + cross);
    _new.set_chromosome(tmp);
    return _new;
}

#endif // GENETIC_OPERATORS_HPP
