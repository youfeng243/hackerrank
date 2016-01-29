#include <iostream>
using namespace std;

class Node
{
public:
    Node()
    {
        mark = 0;
        cnt = 0;
    }
    long long mark;
    long long cnt;        
};

class Tree
{
public:
    Tree( int N )
    {
        pNode = new Node[(N + 100) * 5];
    }
    
    void pushDown( int root )
    {
        if( pNode[root].mark != 0 )
        {
            pNode[root * 2].mark += pNode[root].mark;
            pNode[root * 2 + 1].mark += pNode[root].mark;
            
            pNode[root * 2].cnt += pNode[root].mark;
            pNode[root * 2 + 1].cnt += pNode[root].mark;
            
            pNode[root].mark = 0;
        }
    }
    
    long long insert( int root, int start, int end, int first, int last, long long k )
    {
        if( start > last || end < first )
        {
            return 0;
        }
        
        if( first <= start && last >= end )
        {
            pNode[root].mark += k;
            pNode[root].cnt += k;
            return pNode[root].cnt;
        }
        
        pushDown(root);
        
        int mid = ( start + end ) / 2;
        
        insert( root * 2, start, mid, first, last, k );
        insert( root * 2 + 1, mid + 1, end, first, last, k );
        
        pNode[root].cnt = max(pNode[root * 2].cnt, pNode[root * 2 + 1].cnt);
        return pNode[root].cnt;
    }
    
    long long node( int root )
    {
        return pNode[root].cnt;
    }
    
private:
    Node *pNode;
};

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    int M = 0;
    int a = 0;
    int b = 0;
    long long k = 0;
    
    cin>>N>>M;
    
    Tree *tree = new Tree(N);
    for( int i = 0; i < M; i++ )
    {
        cin>>a>>b>>k;
        if( k != 0 )
        {
            tree->insert( 1, 1, N, a, b, k );
        }
    }  
    
    cout<<tree->node(1)<<endl;
    
    return 0;
}
