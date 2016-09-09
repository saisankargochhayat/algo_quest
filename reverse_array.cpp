#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
    int n,i,x;
    cin>>n;
    vector<int> arr(n);
    for(i=0;i<n;i++)
    {
      cin>>x;
      arr.push_back(x);
    }
    reverse(arr.begin(),arr.end());
    for(i=0;i<n;i++)
    {
      cout<<arr[i];
      cout<<"\n";
    }

  return 0;
}
