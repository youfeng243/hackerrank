/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/


node* insert(node* root, int value)
{
    if( root == NULL )
    {
        node *child = new node();
        child->data = value;
        child->left = NULL;
        child->right = NULL;
        root = child;
        return root;
    }
    
    if( value > root->data )
    {
        root->right = insert(root->right, value);
        return root;
    }
    root->left = insert(root->left, value);
    return root;
}
