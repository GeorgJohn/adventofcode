#include <string>

#include "puzzle.h"



using namespace std;

Puzzle::Puzzle(const char* file_name){
    ifstream file_stream_ = ifstream(file_name, ios::in);
    if (!file_stream_.is_open()) {
        cerr << "Could not open file '" << file_name << "'!" << endl;
        exit(EXIT_FAILURE);
    }
    cout << "Start reading from file: " << file_name << endl;
    this->read_data(file_stream_);

}

Puzzle::~Puzzle(){}


void Puzzle::read_data(ifstream &fs){

    string data_line;
    int n_lines = 0;
    while (getline(fs, data_line))
    {
        data_.push_back(stoi(data_line));
        n_lines++;
    }
    cout << "Successfully read lines: " << n_lines << endl;
}


const int Puzzle::solve(const uint part){

    int fuel = 0;

    for(const int& mass: data_) {

        if (part == 1){
            fuel += (int)mass / 3 - 2;
        }
        else if (part == 2) {
            int residual_fuel = mass;
            while (true) {
                residual_fuel = (int)residual_fuel / 3 - 2;
                if (residual_fuel <= 0)
                    break;
                fuel += residual_fuel;
            }
        }
        else
            fuel = -1;
    }

    return fuel;
}