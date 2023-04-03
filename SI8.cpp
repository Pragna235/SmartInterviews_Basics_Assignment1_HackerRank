//Given two matrices A and B each of size N x M, print sum of the matrices (A + B)..
//Note: Try solving it by declaring only a single matrix.

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    //printf("%d %d",n,m);
    int arr[2*n][m];
    for(int i=0;i<(2*n);i++){
        for(int j=0;j<m;j++){
            scanf("%d",&arr[i][j]);
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            arr[i][j]=arr[i][j]+arr[i+n][j];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }


    return 0;
}

