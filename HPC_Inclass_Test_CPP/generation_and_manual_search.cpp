// Inclass_HPC.cpp

#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

void rand_number_generator(int MIN, int MAX)
{
    std::srand(std::time(nullptr));

    std::ofstream outfile("output.csv");

    for (int i = 0; i < 1000000; ++i) {
        for (int j = 0; j < 20; ++j) {
            outfile << rand() % (MAX - MIN + 1) + MIN;
            if (j != 19)
                outfile << ",";
        }
        outfile << "\n";
    }

    outfile.close();
}


void extract_search_queries(const std::string& filename, const std::vector<int>& indices) {
    std::ifstream file(filename);
    std::string line;
    std::ofstream outfile("search_queries.txt");
    if (file.is_open() && outfile.is_open()) {
        int i = 0;
        while (getline(file, line)) {
            if (std::find(indices.begin(), indices.end(), i) != indices.end()) {
                outfile << line << "\n";
            }
            i++;
        }
        file.close();
        outfile.close();
    }
    else {
        std::cout << "Could not open the file\n";
    }
}

void printIntegerData(const std::vector<std::vector<int>>& data) {
    for (const auto& row : data) {
        for (const auto& element : row) {
            std::cout << element << " ";
        }
        std::cout << "\n";
    }
}

int main()
{
    rand_number_generator(0, 100);
    std::vector<int> search_indices = { 0, 10, 20, 50, 100000, 500000 };
    extract_search_queries("output.csv", search_indices);
    return 0;
}



// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

