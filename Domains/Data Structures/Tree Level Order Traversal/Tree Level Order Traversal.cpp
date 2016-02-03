
void LevelOrder(node* root)
{    
    vector< node* > Q;
    if( root == NULL )
    {
        return;
    }
    
    Q.push_back(root);
    int first = 0;
    int last = 1;
    while( first < last )
    {
        node* temp = Q[first];
        first++;
        
        cout<<temp->data<<" ";
        if( temp->left != NULL )
        {
            Q.push_back(temp->left);
            last++;
        }
        if( temp->right != NULL )
        {
            Q.push_back(temp->right);
            last++;
        }
    }
}
