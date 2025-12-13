#include <bits/stdc++.h>

using namespace std;

int main()
{

    int N = 6;

    std::random_device dev;
    std::mt19937 rng(dev());
    // wstd::uniform_int_distribution<std::mt19937::result_type> dist6(1, 1'000'007); // distribution in range [1, 6]

    vector<int> A;
    for (int i = 0; i < N; i++)
        A.emplace_back(i);

        shuffle(A.begin(), A.end(), rng);

    for (int i = 0; i < N; i++)
        cout << i << " : " << A[i] << "\n";

    return 0;
}