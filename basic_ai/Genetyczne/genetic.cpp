#include <iostream>
#include <vector>

#include "genetic.hpp"
#include "polynomial.hpp"
#include "Pair.hpp"

unsigned int length = 1000;

using namespace std;

vector<Pair> uczacy;

void odczyt(){
  for (int i = 0; i < length; ++i) { 
      double x = 0.0 , y = 0.0;
      cin >> x >> y;
      uczacy.push_back (Pair(x, y));
      cout << "#";
  }
  cout << endl;
}

void printVector(std::vector<Pair> c){
  for (auto tmp : c)
    cout << tmp.getX() << " " << tmp.getY() <<  "\n";
}


int main(){
  cout << "GENETIC ALGORITHM FOR CALCULATING POLYNOMIAL" << endl;
  odczyt();
  printVector(uczacy);
  return 0;
}
