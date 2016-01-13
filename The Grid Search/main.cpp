#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

bool solve( int startx, int starty, int R, int C, char **G, char **P )
{
    for( int i = 0; i < R; i++ )
    {
        for( int j = 0; j < C; j++ )
        {
            if( G[i + startx][j + starty] != P[i][j] )
            {
                return false;
            }
        }
    }
    
    return true;
}

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++)
    {
        int R; 
        int C; 
        scanf("%d %d",&R,&C);
        char* G[R];
        for(int G_i = 0; G_i < R; G_i++){
           G[G_i] = (char *)malloc(1024 * sizeof(char));
           scanf("%s",G[G_i]);
        }
        int r; 
        int c; 
        scanf("%d %d",&r,&c);
        char* P[r];
        for(int P_i = 0; P_i < r; P_i++){
           P[P_i] = (char *)malloc(1024 * sizeof(char));
           scanf("%s",P[P_i]);
        }
        
        bool FindFlag = false;
        for( int i = 0; i < R - r + 1; i++ )
        {
            for( int j = 0; j < C - c + 1; j++ )
            {
                if( solve( i, j, r, c, G, P ) == true )
                {
                    FindFlag = true;
                    break;
                }
            }
            if( FindFlag == true )
            {
                break;
            }
        }
        
        if( FindFlag == true )
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
