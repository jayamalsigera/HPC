#include <mpi.h>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>

std::vector<std::string> readLines(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    std::vector<std::string> lines;

    if (file.is_open()) {
        while (std::getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
    }
    else {
        std::cout << "Unable to open file\n";
    }

    return lines;
}

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Only the root process reads the files
    std::vector<std::string> data;
    std::vector<std::string> queries;
    if (world_rank == 0) {
        data = readLines("output.csv");
        queries = readLines("search_queries.txt");
    }

    int data_per_process = data.size() / world_size;

    std::vector<std::string> local_data(data_per_process);
    MPI_Scatter(data.data(), data_per_process, MPI_CHAR, local_data.data(), data_per_process, MPI_CHAR, 0, MPI_COMM_WORLD);

    for (const auto& query : queries) {
        auto it = std::find(local_data.begin(), local_data.end(), query);
        if (it != local_data.end()) {
            int index = std::distance(local_data.begin(), it);
            std::cout << "Process " << world_rank << " found data set " << query << " in " << index << " : " << *it << "\n";
        }
    }

    MPI_Finalize();
    return 0;
}
