#include <iostream>
#include <stack>
using namespace std;

int main(){
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int N = 0;
    int x = 0;
    int type = 0;
    stack<int> s;
    stack<int> ms;
    
    cin>>N;
    for( int k = 0; k < N; k++ ){
        cin>>type;
        switch( type ){
            case 1:
                cin>>x;
                s.push(x);
                ms.push(max(x, (ms.size() == 0 ? 0 : ms.top())));
                break;
            
            case 2:
                s.pop();
                ms.pop();
                break;
                
            case 3:
                cout<<ms.top()<<endl;
                break;
                
            default:
                break;
        }
    }
    
    return 0;
}
