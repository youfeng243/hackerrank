#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static vector<bool> Beparent;
static vector<bool> Beson;
static map< int, vector<int> > G;
static int cnt = 0;

void DFS( int root, int T )
{
    vector<int>::iterator iter;
    for( iter = G[root].begin(); iter != G[root].end(); iter++ )
    {
        if( abs(root - *iter) <= T )
        {
            cnt++;
        }
        DFS(*iter, T);
    }
}

int main() {
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    
    
    int n = 0;
    int T = 0;
    int x = 0;
    int y = 0;
    
    cin>>n>>T;
    
    Beparent.assign(n + 1, false);
    Beson.assign(n + 1, false);
    
    for( int i = 0; i < n - 1; i++ )
    {
        cin>>x>>y;
        G[x].push_back(y);
        Beparent[x] = true;
        Beson[y] = true;
    }
    
    if( n <= 1 )
    {
        printf("0\n");
        return 0;
    }
    
    int root = 0;
    for( int i = 1; i <= n; i++ )
    {
        if( Beson[i] == false )
        {
            root = i;
            break;
        }
    }
    
    DFS(root, T);
    
    cout<<cnt<<endl;
    
    return 0;
}
