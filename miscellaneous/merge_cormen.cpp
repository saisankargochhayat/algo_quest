#include<iostream>
using namespace std;
void merge(int A[],int p,int q,int r)
{ int n1=q-p+1;
  int n2=r-q;
  int L[n1],R[n2],i,j;
  for(i=0;i<n1;i++)
  {
    L[i]=A[p+i];
  }
  for(j=0;j<n2;j++)
  {
    R[j]=A[q+1+j];
  }
i=0;j=0;int k=p;
while(i<n1 && j<n2)
{
  if(L[i]<=R[j])
    {
      A[k]=L[i];
      i++;
    }
  else
    {
      A[k]=R[j];
      j++;
    }
    k++;
}
while(i<n1)
{
  A[k]=L[i];
  i++;
  k++;
  }
while(j<n2)
{
  A[k]=R[j];
  j++;
  k++;
}

}



void mergesort(int A[],int p,int r)
{
  if(p<r)
{  int q=(p+r)/2;
    mergesort(A,p,q);
    mergesort(A,q+1,r);
    merge(A,p,q,r);
}
}
void printArray(int A[],int size)
{
  int i;
  for(i=0;i<size;i++)
  {
      cout<<A[i];
  }
  cout<<"\n";
}

int main()
{
  int A[]={4,1,3,6,8,9};
  int size=sizeof(A)/sizeof(A[0]);
  
  printArray(A,size);
  mergesort(A,0,size-1);
  printArray(A,size);
  return 0;

}
