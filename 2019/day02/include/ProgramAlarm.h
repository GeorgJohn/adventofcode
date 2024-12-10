#ifndef PROGRAMALARM_H_
#define PROGRAMALARM_H_

#include <fstream>
#include <iostream>
#include <vector>


using namespace std;

class ProgramAlarm
{
private:
    
    vector<int> data_;

    void read_data(ifstream &fs);

public:

    ProgramAlarm(const char* file_name);
    ~ProgramAlarm();

    const int solve(const uint part);

};

#endif //PROGRAMALARM_H_