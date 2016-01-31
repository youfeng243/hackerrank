#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int global[5001][5001] = {0};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    freopen("in.txt","r", stdin);
    freopen("out.txt", "w", stdout);
    
    string A;
    string B;
    cin>>A>>B;
    
    //memset(global, 0, sizeof(global));
    
    for( int i = 1; i <= A.length(); i++ )
    {
        for( int j = 1; j <= B.length(); j++ )
        {
            if( A[i - 1] == B[j - 1] )
            {
                global[i][j] = global[i - 1][j - 1] + 1;
            }
            else
            {
                global[i][j] = max(global[i - 1][j], global[i][j - 1]);
            }
        }
    }
    
    cout<<global[A.length()][B.length()]<<endl;
    //cout<<A<<endl<<B<<endl;
    
    return 0;
}
