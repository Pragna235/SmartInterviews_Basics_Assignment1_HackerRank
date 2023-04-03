//Given a matrix of size N x M, print whether it is a sparse matrix or not.
//Note: If a matrix contain 0 in more than half of its cells, then it is called a sparse matrix.

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,m,count=0;
    cin>>n>>m;
    int arr[n][m];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>arr[i][j];
            if(arr[i][j]==0)
                count++;
        }
    }
    if(count>((n*m)/2))
        cout<<"Yes";
    else
        cout<<"No";

    return 0;
}

