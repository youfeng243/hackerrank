#include <iostream>
using namespace std;

class Node{
public:
    Node(){
        m_left = -1;
        m_right = -1;
    }
    
    void setLeft( int left ){
        m_left = left; 
    }
    
    void setRight( int right ){
        m_right = right;
    }
    
    int getLeft( void ){
        return m_left;
    }
    
    int getRight( void ){
        return m_right;
    }
    
private:
    int m_left;
    int m_right;
};

Node nodes[1025];

void Change( int root, int curdeep, const int deep ){
    
    int curleft = nodes[root].getLeft();
    int curright = nodes[root].getRight();
    
    if( curdeep % deep == 0 ){    
        nodes[root].setLeft(curright);
        nodes[root].setRight(curleft);
    }
    
    if( curleft != -1 ){
        Change(curleft, curdeep + 1, deep);
    }
    
    if( curright != -1 ){
        Change(curright, curdeep + 1, deep);
    }
}

void Visit( const int root ){
    if( root == -1 ){
        return;
    }
    
    Visit( nodes[root].getLeft() );
    cout<<root<<" ";
    Visit( nodes[root].getRight() );
}

int main(){
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    int a = 0;
    int b = 0;
    int T = 0;
    int K = 0;
    
    cin>>N;
    for( int i = 1; i <= N; i++ ){
        cin>>a>>b;
        nodes[i].setLeft(a);
        nodes[i].setRight(b);
    }
    
    cin>>T;
    for( int i = 0; i < T; i++ ){
        cin>>K;
        Change( 1, 1, K );
        Visit(1);
        cout<<endl;
    }
    
    return 0;
}
