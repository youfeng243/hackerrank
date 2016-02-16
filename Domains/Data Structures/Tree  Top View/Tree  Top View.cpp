void top_view(node * root)
{
    vector<int> array;
    node *point = NULL;
    if( root == NULL )
    {
        return;
    }
    
    if( root->left != NULL )
    {
        point = root;
        while( point->left != NULL )
        {
            point = point->left;
            array.push_back(point->data);
        }
        for( int i = array.size() - 1; i >= 0; i-- )
        {
            cout<<array[i]<<" ";
        }
        array.clear();
    }
    
    point = root;
    array.push_back(root->data);
    if( root->right != NULL )
    {
        while( point->right != NULL )
        {
            point = point->right;
            array.push_back(point->data);
        }
    }
    
    for( int i = 0; i < array.size(); i++ )
    {
        cout<<array[i]<<" ";
    }
}
