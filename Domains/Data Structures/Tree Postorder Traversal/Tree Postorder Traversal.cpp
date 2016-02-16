void Postorder(node *root) {
    if( root == NULL )
    {
        return;
    }
    
    Postorder(root->left);
    Postorder(root->right);
    cout<<root->data<<" ";
}
