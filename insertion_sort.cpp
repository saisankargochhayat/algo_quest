#include <iostream>
using namespace std;
int main()
{
    int i,j,k,n,temp,key;
    cin>>n;
    int A[n];
    cout<<"enter the elements";
    for(i=0;i<n;i++)
    {
        cin>>A[i];

    }
    for(int j=1; j<n; j++){ //Iterate through the Array.
    int key = A[j]; //Store the current element into key.
    int i = j-1; //Iterator for while loop.
    while(i>-1 && A[i]>key){ //Loop to insert A[j] into the sorted sequence.
      A[i+1] = A[i]; //Move the element.
      i=i-1; //New value of i.
      A[i+1] = key; //Update the key
    }
  }
    for(i=0;i<n;i++)
    {
        cout<<A[i];

    }
}







