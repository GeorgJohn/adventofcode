cmake_minimum_required(VERSION 3.0.0)
project(1220_program_alarm 
    VERSION 0.1.0
    LANGUAGES CXX
    )

add_library(ProgramAlarm
    STATIC 
    src/ProgramAlarm.cpp
    )

target_include_directories(ProgramAlarm 
    PUBLIC include
    )

add_executable(program_alarm main.cpp)

target_link_libraries(program_alarm
    PRIVATE ProgramAlarm
    )
