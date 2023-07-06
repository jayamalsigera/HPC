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
    MPI_Init(&argc, &argv);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    std::vector<std::string> data;
    std::vector<std::string> queries;

    if (world_rank == 0) {
        data = readLines("output.csv");
        queries = readLines("search_queries.txt");
    }

    // Broadcasting the size of the queries
    int queries_size = queries.size();
    MPI_Bcast(&queries_size, 1, MPI_INT, 0, MPI_COMM_WORLD);
    if(world_rank != 0) {
        queries.resize(queries_size);
    }

    // Broadcasting the queries
    for(int i = 0; i < queries_size; ++i) {
        int buffer_size = queries[i].size() + 1; // +1 for '\0'
        MPI_Bcast(&buffer_size, 1, MPI_INT, 0, MPI_COMM_WORLD);

        if(world_rank != 0) {
            queries[i].resize(buffer_size - 1);
        }

        MPI_Bcast(&queries[i][0], buffer_size, MPI_CHAR, 0, MPI_COMM_WORLD);
    }

    int data_per_process = data.size() / world_size;
    int remainder = data.size() % world_size;

    // calculate count and displacement arrays for scatterv
    std::vector<int> counts(world_size);
    std::vector<int> displs(world_size);
    int sum = 0;
    for(int i = 0; i < world_size; ++i) {
        counts[i] = (i < remainder) ? data_per_process + 1 : data_per_process;
        displs[i] = sum;
        sum += counts[i];
    }

    int local_data_count = counts[world_rank];
    std::vector<std::string> local_data(local_data_count);
    MPI_Scatterv(data.data(), counts.data(), displs.data(), MPI_CHAR, local_data.data(), local_data_count, MPI_CHAR, 0, MPI_COMM_WORLD);

    for (const auto& query : queries) {
        auto it = std::find(local_data.begin(), local_data.end(), query);
        if (it != local_data.end()) {
            int index = std::distance(local_data.begin(), it);
            std::cout << "Process " << world_rank << " found data set " << query << " at index " << index << " : " << *it << "\n";
        }
    }

    MPI_Finalize();
    return 0;
}
