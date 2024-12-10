#ifndef PUZZLE_H_
#define PUZZLE_H_

#include <fstream>
#include <iostream>
#include <vector>


using namespace std;

class Puzzle
{
private:
    
    vector<int> data_;

    void read_data(ifstream &fs);

public:

    Puzzle(const char* file_name);
    ~Puzzle();

    const int solve(const uint part);

};

#endif //PUZZLE_H_