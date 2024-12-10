cmake_minimum_required(VERSION 3.12.0)

project(aoc_2019_01
    VERSION 0.1.0
    DESCRIPTION "Advent of Code 2019 day 01"
    LANGUAGES CXX
    )

add_library(puzzle
    STATIC
    src/puzzle.cpp
    )

target_include_directories(puzzle 
    PUBLIC include
    )

add_executable(solve_day01 main.cpp)

target_link_libraries(solve_day01
    PRIVATE puzzle
    )