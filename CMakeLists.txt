cmake_minimum_required(VERSION 3.4)
project(glxgears)

set(CMAKE_C_STANDARD 11)

set(CMAKE_C_FLAGS "-Wall -O2")
set(CMAKE_CXX_FLAGS "-Wall -O2")

add_executable(glxgears glxgears.c)
target_link_libraries(glxgears -lGL -lX11 -lpthread -lXrandr -lXi -ldl -lm -lgsl)

