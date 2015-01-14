#ifndef DRAW_HANDLER_HPP
#define DRAW_HANDLER_HPP

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include "chromosome.hpp"
#include <iostream>
#include "Pair.hpp"

using namespace std;

#define SIZE 512
#define ITERATION 10000000

int fraktal[SIZE][SIZE];
Pair wsp [SIZE][SIZE];

int fraktal1[SIZE][SIZE];
Pair wsp1 [SIZE][SIZE];

void sierpinski() {
    double x=0,y=0;
    for(int i = 0;i < ITERATION; i++) {
        int zabarwienie;
        switch(rand() % 3) {
           case 0: x = x / 2;
                   y = y / 2;
                   zabarwienie = 55;
                   break;
           case 1: x = x / 2 + 0.25;
                   y = y / 2 + 0.25 * sqrt(3.0);
                   zabarwienie = 155;
                   break;
            case 2: x = x / 2 + 0.5;
                    y = y / 2;
                    zabarwienie = 255;
                    break;

       }
    fraktal[(int)(x * SIZE)][(int)(y * SIZE)] = zabarwienie;
    wsp[(int)(x * SIZE)][(int)(y * SIZE)] = Pair((int)(x * SIZE),(int)(y * SIZE));
  }
}

void sierpinski1(int a, int b, int c, int d, int e, int f, int g, int h, int j, int k, int l, int m) {
    double x=0,y=0;
    for(int i = 0;i < ITERATION; i++) {
        int zabarwienie;
        switch(rand() % 3) {
           case 0: x = x * a + b;
                   y = y * c  + d;
                   zabarwienie = 55;
                   break;
           case 1: x = x * e + f;
                   y = y * g + h;
                   zabarwienie = 155;
                   break;
            case 2: x = x * j + k;
                    y = y * l + m;
                    zabarwienie = 255;
                    break;

       }
    fraktal1[(int)(x * SIZE)][(int)(y * SIZE)] = zabarwienie;
    wsp1[(int)(x * SIZE)][(int)(y * SIZE)] = Pair((int)(x * SIZE),(int)(y * SIZE));
  }
}

void draw(int array[SIZE][SIZE]){
    FILE *image = fopen("fractal.pgm","w+");
    fprintf(image,"P2\n%d %d\n255\n",SIZE, SIZE);

    for(int i=SIZE-1;i>=0;i--){
        for(int j=0;j<SIZE;j++){
            fprintf(image,"%d ",array[j][i]);
            cout << wsp[j][i].x  << " "  << wsp[j][i].y << " ";
        }
    fprintf(image,"\n");
    cout << "\n";
  }
}

#endif // DRAW_HANDLER_HPP
