#include <iostream>
#include <stack>
using namespace std;

int main(){
    
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    string str = "";
    int N = 0;
    bool flag = true;
    stack<char> s;
    
    cin>>N;
    for( int k = 0; k < N; k++ ){
        cin>>str;
        
        flag = true;
        while( s.empty() == false ) s.pop();
        for( int i = 0; i < str.length(); i++ ){
            if( s.empty() == true ){
                s.push(str[i]);
                continue;
            }
            if( ( str[i] == ')' && s.top() == '(' ) || 
                ( str[i] == ']' && s.top() == '[' ) ||
                ( str[i] == '}' && s.top() == '{' ) ){
                    s.pop();
                    continue;
                }
            if( str[i] == '(' || str[i] == '[' || str[i] == '{' ){
                s.push(str[i]);
                continue;
            }
            flag = false;
            break;
        }
        if( flag == false || s.empty() == false ){
            cout<<"NO"<<endl;
        } else {
            cout<<"YES"<<endl;
        }
    }
    
    return 0;
}
