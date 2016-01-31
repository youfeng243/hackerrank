#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int nextA[100005]; 
int nextB[100005];

int main() 
{
    int T = 0;
    string A = "";
    string B = "";
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    cin>>T;
    
    for( int t0 = 0; t0 < T; t0++ )
    {
        cin>>A;
        cin>>B;
        
        int i = 0;
        int j = 0;
        
        int lengthA = A.length();
        int lengthB = B.length();
        
        //memset(nextA, 0, sizeof(nextA));
        //memset(nextB, 0, sizeof(nextB));
        
        nextA[lengthA - 1] = 0;
        nextB[lengthB - 1] = 0;
        
        for( int k = lengthA - 2; k >= 0; k-- )
        {
            if( A[k] == A[k + 1] )
            {
                nextA[k] = nextA[k + 1] + 1;
            }
            else
            {
                nextA[k] = 0;
            }
        }
        
        /*
        cout<<A<<endl;
        for( int k = 0; k < lengthA; k++ )
        {
            cout<<nextA[k];
        }
        cout<<endl;
        */
        
        
        for( int k = lengthB - 2; k >= 0; k-- )
        {
            if( B[k] == B[k + 1] )
            {
                nextB[k] = nextB[k + 1] + 1;
            }
            else
            {
                nextB[k] = 0;
            }
        }
        
        /*
        cout<<B<<endl;
        for( int k = 0; k < lengthB; k++ )
        {
            cout<<nextB[k];
        }
        cout<<endl;
        */
        
        while( i < lengthA || j < lengthB )
        {
            if( i >= lengthA )
            {
                cout<<B.substr(j);
                break;
            }
            if( j >= lengthB )
            {
                cout<<A.substr(i);
                break;
            }
            
            int tempi = i;
            int tempj = j;
          
            bool get1 = true;
            while( tempi < lengthA && tempj < lengthB )
            {
                int minstep = min(nextA[tempi], nextB[tempj]);
                tempi += minstep;
                tempj += minstep;
                
                if( A[tempi] == B[tempj] )
                {
                    //int minstep = min(nextA[tempi], nextB[tempj]) + 1;
                    //tempi += minstep;
                    //tempj += minstep;
                    
                    tempi++;
                    tempj++;
                    
                    if( tempi >= lengthA )
                    {
                        get1 = false;
                    }
                    else if ( tempj >= lengthB )
                    {
                        get1 = true;
                    }
                    
                    continue;
                }
                if( A[tempi] < B[tempj] )
                {
                    get1 = true;
                    break;
                }
                get1 = false;
                break;
            }
            
            /*
            if( tempi >= lengthA && tempj >= lengthB )
            {
                get1 = true;
            }
            else if( tempi >= lengthA && tempj < lengthB )
            {
                get1 = false;
            }
            else if( tempi < lengthA && tempj >= lengthB )
            {
                get1 = true;
            }
            */
            
            if( get1 == true )
            {
                cout<<A[i];
                i++;
            }
            else
            {
                cout<<B[j];
                j++;
            }
        }
        cout<<endl;  
    }
    return 0;
}
