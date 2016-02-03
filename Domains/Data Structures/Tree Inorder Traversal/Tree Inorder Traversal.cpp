void Inorder(node *root) {
    if( root == NULL )
    {
        return;
    }
    
    Inorder(root->left);
    cout<<root->data<<" ";
    Inorder(root->right);   
}
