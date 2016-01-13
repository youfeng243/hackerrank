#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool used[100005] = {false};
int sum[100005] = {0};
int weight[100005] = {0};
map< int, vector<int> > G;

int DFS( int start, int N )
{
    if( start > N )
    {
        return 0;
    }
    
    /*
    if( G.count(start) <= 0 )
    {
        return sum[start];
    }
    */
    
    vector<int>::iterator iter;
    for( iter = G[start].begin(); iter != G[start].end(); iter++ )
    {
        if( used[*iter] == true )
        {
            continue;
        }
        used[*iter] = true;
        sum[start] += DFS(*iter, N);
    }
    
    return sum[start];
}

int main() {
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int X = 0;
    int Y = 0;
    int N = 0;
    int Min = 100000000;
    
    cin>>N;
    
    for( int i = 0; i < N; i++ )
    {
        cin>>weight[i + 1];
        sum[i + 1] = weight[i + 1];
    }
    
    for( int i = 0; i < N - 1; i++ )
    {
        cin>>X>>Y;
        G[X].push_back(Y);
        G[Y].push_back(X);
    }
    
    used[1] = true;
    DFS(1, N);
    
    for( int i = 2; i <= N; i++ )
    {
        int temp = abs(sum[1] - 2 * sum[i]);
        if( temp < Min )
        {
            Min = temp;
        }    
    } 
    
    cout<<Min<<endl;
    
    return 0;
}
