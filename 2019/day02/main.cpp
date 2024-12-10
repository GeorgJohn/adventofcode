#include <iostream>
#include <fstream>

# include "include/ProgramAlarm.h"


using namespace std;


int main(int argc, char *argv[]) {

    if (argc <= 1) {
        cout << "Please enter at least one file path." << endl;
    }
    else {
        for (auto i = 1; i < argc; ++i) {
            
            ProgramAlarm puzzle(argv[i]);
            
            int solution1 = puzzle.solve(1);
            int solution2 = puzzle.solve(2);

            cout <<  endl;
            cout << argv[i] << endl;
            cout << "The puzzle solution of part 1 is: " << solution1 << endl;
            cout << "The puzzle solution of part 2 is: " << solution2 << endl;
        }  
    }
    return EXIT_SUCCESS;
}