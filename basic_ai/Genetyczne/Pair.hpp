#ifndef _PAIR_HPP_
#define _PAIR_HPP_

class Pair {
  private:
    double x; 
    double y;
  public: 
    double getX();
    double getY();
    void setX(double x);
    void setY(double y);
    Pair(double _x, double _y) : x(_x), y(_y) {};

};

#endif
