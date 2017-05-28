#include <iostream>
#include <vector>

using namespace std;

struct snake{
    int hx,hy,tx,ty;
};

void rearrange(vector<snake> s,vector<int> &h,vector<int> &v,long start,long end){
  for(int i=0;i<s.size();i++){
    if(s[i].hx==s[i].tx){
      if(s[i].hy>=start && s[i].hy<=end){
        for(int j=(s[i].hy - start);j<=(s[i].ty - start) && j<h.size();j++){
          if((s[i].ty - start - j + 1) > h[j])
            h[j] = s[i].ty - start - j + 1;
        }
      }
      else if(s[i].ty>=start && s[i].ty<=end){
        for(int j=0;j<=(s[i].ty - start);j++){
          if((s[i].ty - start - j + 1) > h[j])
            h[j] = s[i].ty - start - j + 1;
        }
      }
      else if(s[i].hy<=start && s[i].ty>=end){
        for(int j=0;j<h.size();j++){
          if((s[i].ty - start - j + 1) > h[j])
            h[j] = s[i].ty - start - j + 1;
        }
      }
      else if(s[i].hx>=start && s[i].hx<=end){
        if(v[s[i].hx-start]==0)
          v[s[i].hx-start]=1;
      }
    }

    else{
      if(s[i].hx>=start && s[i].hx<=end){
        for(int j=(s[i].hx - start);j<=(s[i].tx - start) && j<v.size();j++){
          if((s[i].tx - start - j + 1) > v[j])
            v[j] = s[i].tx - start - j + 1;
        }
      }
      else if(s[i].tx>=start && s[i].tx<=end){
        for(int j=0;j<=(s[i].tx - start);j++){
          if((s[i].tx - start - j + 1) > v[j])
            v[j] = s[i].tx - start - j + 1;
        }
      }
      else if(s[i].hx<=start && s[i].tx>=end){
        for(int j=0;j<v.size();j++){
          if((s[i].tx - start - j + 1) > v[j])
            v[j] = s[i].tx - start - j + 1;
        }
      }
      else if(s[i].hy>=start && s[i].hy<=end){
        if(h[s[i].hy-start]==0)
          h[s[i].hy-start]=1;
      }
    }
  }
}

int find_minimum_snakes(vector<int> &h,vector<int> &v){
  int min_snakes = 0;
  for(int i=0;i<h.size();){
    if(h[i]==0)
      return -1;
    else{
      i+=h[i];
      min_snakes++;
    }
  }
  for(int i=0;i<v.size();){
    if(v[i]==0)
      return -1;
    else{
      i+=v[i];
      min_snakes++;
    }
  }
  return min_snakes;
}

int main() {
  int t;
  cin>>t;
  while(t){
    long n,k;
    int m;
    cin>>n>>k>>m;
    vector<snake> snakes(m);
    for(int i=0;i<m;i++){
      cin>>snakes[i].hx>>snakes[i].hy>>snakes[i].tx>>snakes[i].ty;
    }
    vector<int> hor(k);
    vector<int> vert(k);
    rearrange(snakes,hor,vert,((n-k)/2 + 1),((n+k)/2));
    int min_snakes = find_minimum_snakes(hor,vert);
    // cout<<"horizontal_exc:"<<endl;
    // for(int i=0;i<hor_exc.size();i++){
    //   cout<<hor_exc[i].hx<<" "<<hor_exc[i].hy<<" "<<hor_exc[i].tx<<" "<<hor_exc[i].ty<<" "<<hor_exc[i].used<<endl;
    // }
    cout<<min_snakes<<endl;
    t--;
  }
  return 0;
}
