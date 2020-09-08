/*
*
*	Created By: r3gz3n
*	Description: Ad-Hoc, Preprocessing
*   Expected Complexity: Preprocessing = O(26*N), Queries = O(26)
*
*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <istream>
#include <ostream>
#include <fstream>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <stack>
#include <queue>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <cctype>
#include <climits>
#define ll long long
#define ull unsigned long long
using namespace std;
const int MAX = 50005;
int A[MAX][26];
int main()
{

    int queries, len, left, right, k, x, K;
    string str;
    char ans;


    cin >> len >> queries >> str;

    str = "0" + str;        // Indexing is starts from 1

    // Preprocessing : Calculating prefix sum
    for(int i = 1;i <= len;++i)
    {
        x = str[i] - 'a';

        // Counting Frequencies of each character in the prefix of str
        for(int j = 0;j < 26;++j)
            if(j == x) A[i][j] = A[i-1][j] + 1;
            else A[i][j] = A[i-1][j];
    }


    // Queries
    for(int i = 0, j;i < queries;++i)
    {
        cin >> left >> right >> k;

        // Counting the Kth smallest character
        K = 0;
        for(j = 0;j < 26;++j)
        {
            K += A[right][j] - A[left-1][j];
            if(K >= k)
                break;
        }

        ans = 'a' + j;
        if(j == 26) cout << "Out of range" << endl;
        else cout << ans << endl;

    }

    return EXIT_SUCCESS;
}
