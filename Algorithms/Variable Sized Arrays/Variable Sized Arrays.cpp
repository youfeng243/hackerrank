#include <iostream>
#include <vector>
using namespace std;

//int Array[100001][300];

int main() 
{
    int N = 0;
    int Q = 0;
    int K = 0;
    
    int num = 0;
    
    int ArrayIndex = 0;
    int Index = 0;
    
    
    
    
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    cin>>N>>Q;
    
    int **Array = new int*[N + 1];
    
    //std::vector<std::vector<int> > Array;
    for( int i = 0; i < N; i++ )
    {
        cin>>K;
        
        Array[i] = new int[K + 1];
        //std::vector<int> temp;
        
        for( int j = 0; j < K; j++ )
        {
            cin>>Array[i][j];
            
            //temp.push_back(num);
        }
        //Array.push_back(temp);
    }
    
    for( int i = 0; i < Q; i++ )
    {
        cin>>ArrayIndex>>Index;
        cout<<Array[ArrayIndex][Index]<<endl;
    }
    
    
    return 0;
}
    
