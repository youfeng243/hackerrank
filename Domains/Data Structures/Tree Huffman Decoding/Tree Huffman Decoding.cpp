
/* 
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;

*/


void decode_huff(node * root,string s){
    if( root == NULL ){
        return;
    }
    int i = 0;
    int length = s.length();
    
    while( i < length ){
        node *point = root;
        while( i < length ){
            if( s[i] == '1' ){
                point = point->right;
            }
            else{
                point = point->left;
            }
            i++;
            
            if( point->left == NULL && point->right == NULL ){
                cout<<point->data;
                break;
            }
            
        }
    }
    cout<<endl;
}
