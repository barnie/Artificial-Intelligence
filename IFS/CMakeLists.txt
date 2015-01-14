cmake_minimum_required (VERSION 2.6)
project (ReverseIFS)

SET (CMAKE_CXX_COMPILER             "/usr/bin/clang++")
SET (CMAKE_CXX_FLAGS                "-Wall")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
add_executable(ReverseIFS main.cpp chromosome.hpp Pair.cpp draw_handler.hpp)
