#include <iostream>
#include <vector>
using namespace std;

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    int M = 0;
    int a = 0;
    int b = 0;
    long long k = 0;
    vector<long long> array;
    
    cin>>N>>M;
    array.assign( N + 2, 0 );
    
    for( int i = 0; i < M; i++ )
    {
        cin>>a>>b>>k;
        array[a] += k;
        array[b + 1] += -k;
    }
    
    /*
    for( int i = 1; i <= N; i++ )
    {
        cout<<array[i]<< " ";
    }
    cout<<endl;
    */
    
    long long Max = 0;
    for( int i = 1; i <= N; i++ )
    {
        array[i] += array[i - 1];
        Max = max( Max, array[i] );
    }
    
    cout<<Max<<endl;
    return 0;
}
