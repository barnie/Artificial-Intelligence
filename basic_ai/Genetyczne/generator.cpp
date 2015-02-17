#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <iomanip>
#include "polynomial.hpp"

using namespace std;

//okreslenie przedzialu:
double MAX = 2.0;
double MIN = -2.0;



double get_random(){
  return (MAX - MIN) * ( (double)rand() / (double)RAND_MAX ) + MIN;
}
 
int main(){
  srand(time(NULL));
  for (int i = 0; i < 1000; ++i){
    double tmp = get_random();
    cout << std::fixed << setprecision(5) << tmp << " " << rownanie(tmp) << endl;
  }
  return 0;
}

