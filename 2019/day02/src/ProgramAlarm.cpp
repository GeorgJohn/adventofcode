#include <string>
#include <sstream>
#include "ProgramAlarm.h"



using namespace std;

ProgramAlarm::ProgramAlarm(const char* file_name){
    ifstream file_stream_ = ifstream(file_name, ios::in);
    if (!file_stream_.is_open()) {
        cerr << "Could not open file '" << file_name << "'!" << endl;
        exit(EXIT_FAILURE);
    }
    this->read_data(file_stream_);

}

ProgramAlarm::~ProgramAlarm(){}


void ProgramAlarm::read_data(ifstream &fs){

    string program;
    int n_lines = 0;
    // only read first line
    getline(fs, program);
    // convert string in stringstream
    stringstream ss_program(program);
    // read data
    string num;
    while (getline(ss_program, num, ',')) {
        data_.push_back(stoi(num));
    }
}


const int ProgramAlarm::solve(const uint part){

    vector<int> program(data_);

    int program_len = program.size() / 4;

    for (int n=0; n < program_len; ++n) {
        int operation = program[4*n];
        int input_idx_1 = program[4*n+1];
        int input_idx_2 = program[4*n+2];
        int output_idx = program[4*n+3];

        if (operation == 1) {
            program[output_idx] = program[input_idx_1] + program[input_idx_2];
        }
        else if (operation == 2) {
            program[output_idx] = program[input_idx_1] * program[input_idx_2];
        }
    }
    // for (auto num : program) {
    //     cout << num << " ";    
    // }
    // cout << endl;
    return program[0];
}