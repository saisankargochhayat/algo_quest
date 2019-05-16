#include <iostream>
#include <cassert>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <set>
#define MAXFIBO 65
#define ll long long
using namespace std;

ll F[MAXFIBO+1];
ll ComputeSum(ll N) {
    ll ans = 0;
    ll x = 1;
    while(x <= N) {
        // N/x
        // max y st N/y >= N/x
        // y <= N/(N/x+1)
        ll y;
        if (x == N)
            y=N;
        else
            y = min(N,N/(N/x));
        ans += (y-x+1)*(N/x);
        x = y+1;
    }
    return ans;
}

long long kgcd(long long a, long long b)
{
    while (a > 0 && b > 0)
    {
        a -= b;
        swap(a , b);
    }
    return a + b;
}

int main() {
    F[0]=0;
    F[1]=1;
    for(int i=2;i<=MAXFIBO;i++)
        F[i]=(F[i-1]+F[i-2]);


    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        ll N;
        cin>>N;




        if (N == 1) {
            cout << 1 << endl;
            continue;
        }

        ll ans = 2*(ComputeSum(N)-N) + N;


        for(ll jmax=2;jmax<=MAXFIBO;jmax++) {

            ll k = 2;
            while(1) {
                if (N  < (k*F[jmax]+F[jmax-1]))
                    break;

                ll xmax = N / (k*F[jmax]+F[jmax-1]);

                // Find minimum kmax such that

                // xmax * (kmax*F[jmax]+F[jmax-1]) <= N


                ll kmax = (N - xmax*F[jmax-1]) / (xmax*F[jmax]);
                ans += (kmax-k+1)*xmax;
                k = kmax+1;
            }



        }
        cout << ans << endl;

    }

}
