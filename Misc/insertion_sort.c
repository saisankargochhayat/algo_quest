#include <iostream>
using namespace std;
int main()
{
    int a[],i,j,k,n;
    cin>>n;
    cout<<"enter the elements";
    for(i=0;i<n;i++)
    {
        cin>>a[i];

    }
    for(int j=2;j<a.length();j++)
    {
        k=a[j];
        i=j-1;
        while((i>0)&&(a[i]>k))
        {
            a[i+1]=a[i];
            i=i-1;
        }

         a[i+1]=k;
    }
}







