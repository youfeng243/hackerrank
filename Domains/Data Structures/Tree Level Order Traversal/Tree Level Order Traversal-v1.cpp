#include <queue>

void LevelOrder(node* root)
{    
    queue< node* > Q;
    if( root == NULL )
    {
        return;
    }
    
    Q.push(root);
    while( Q.empty() == false )
    {
        node* temp = Q.front();
        Q.pop();
        
        cout<<temp->data<<" ";
        if( temp->left != NULL )
        {
            Q.push(temp->left);
        }
        if( temp->right != NULL )
        {
            Q.push(temp->right);
        }
    }
}
