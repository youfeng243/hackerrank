#include <iostream>
#include <vector>
using namespace std;


//Node is defined as 
typedef struct node
{
   int data;
   node* left;
   node* right;
}node;


int findpath( node* root, int value, int index, vector<node*> &path ){
    
    int length = 0;
    
    if( root == NULL ){
        return -1;
    }

    if( path.size() <= index ){
        path.push_back(root);
    } else {
        path[index] = root;
    }
    
    if( root->data == value ){ 
        return index + 1;
    }
    
    if( root->right ){
        length = findpath(root->right, value, index + 1, path);
        if( length > 0 ){
            return length;
        }
    }

    if( root->left ){
        length = findpath(root->left, value, index + 1, path);
        if( length > 0 ){
            return length;
        }   
    }    
    return -1;
}

node* lca(node* root, int v1,int v2){
    
    int i = 0;
    node* common = NULL;
    vector<node*> path1;
    vector<node*> path2;
    
    int length1 = findpath( root, v1, 0, path1 );
    int length2 = findpath( root, v2, 0, path2 );
    
    i = 0;
    while( i < length1 && i < length2 ){
        if (path1[i]->data == path2[i]->data){
            common = path1[i];
            i++;
            continue;
        }
        break;
    }

    return common;
}

node *BinaryTree( node* root, int value ){
    if( root == NULL ){
        node *pNode = new node();
        pNode->data = value;
        pNode->left = NULL;
        pNode->right = NULL;
        return pNode;
    }
    
    if( root->data > value ){
        root->left = BinaryTree(root->left, value);
    }
    else {
        root->right = BinaryTree( root->right, value );
    }
    
    return root;
}

int main(){
    
    freopen("out.txt", "w", stdout);
    
    int A[6] = {4, 2, 3, 1, 7, 6};
    
    node *root = NULL;
    for( int i = 0; i < 6; i++ ){
        root = BinaryTree(root, A[i]);
    }
    
    node *common = lca(root, 1, 7);
    if( common != NULL ){
        cout<<common->data<<endl;
    } else {
        cout<<"NULL"<<endl;
    }
    
    return 0;
}
