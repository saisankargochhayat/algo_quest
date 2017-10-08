#include <iostream>
using namespace std;
int main()
{
    int i,j,k,n,temp;
    cin>>n;
    int a[n];
    cout<<"enter the elements";
    for(i=0;i<n;i++)
    {
        cin>>a[i];

    }
    for (i = 1; i < n; i++)
    {
        for (j = i; j >= 1; j--)
        {
            if (a[j] < a[j-1])
            {
                temp = a[j];
                a[j] = a[j-1];
                a[j-1] = temp;
            }
            else
                break;
        }
    }
    for(i=0;i<n;i++)
    {
        cout<<a[i];

    }
}







