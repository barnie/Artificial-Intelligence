cmake_minimum_required (VERSION 2.6)
project (Genetyczne)

SET(CMAKE_CXX_FLAGS "-std=c++0x")

add_executable(genetic genetic.cpp Pair.cpp)
add_executable(generator generator.cpp)
