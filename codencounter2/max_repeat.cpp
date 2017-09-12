#include<bits/stdc++.h>
using namespace std;
 
// Returns the maximum repeating character in a
// given string
int maxRepeating(string str)
{
    int n = str.length();
    int count = 0;
    char res = str[0];
    int cur_count = 1;
 
    // Traverse string except last character
    for (int i=0; i<n; i++)
    {
        // If current character matches with next
        if (i < n-1 && str[i] == str[i+1])
            cur_count++;
 
        // If doesn't match, update result
        // (if required) and reset count
        else
        {
            if (cur_count > count)
            {
                count = cur_count;
                res = str[i];
            }
            cur_count = 1;
        }
    }
    return count;
}
 
// Driver code
int main()
{
    string raw;
    std::getline(std::cin,raw);
    cout << maxRepeating(raw);    
    return 0;
}