int height(node * root)
{
    if( root == NULL )
    {
        return 0;
    } 
    
    return max( height(root->left), height(root->right) ) + 1;
}
