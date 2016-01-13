#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int T = 0;
    unsigned int N = 0;
    unsigned int INF = 0;
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
      
    for( int i = 0; i < 32; i++ )
    {
        INF <<= 1;
        INF += 1;
    }
  
    cin>>T;
    
    while( T-- )
    {
        cin>>N;
        
        cout<<(N^INF)<<endl;
    }
      
    return 0;
}
