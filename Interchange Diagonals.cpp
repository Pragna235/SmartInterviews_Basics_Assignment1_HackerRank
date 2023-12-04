#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    
    int mat[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>mat[i][j];
        }
    }
    
    int res[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j){
                res[i][j]=mat[i][n-1-i];
            }
            else if((i+j)==n-1){
                res[i][j]=mat[i][i];
            }
            else{
                res[i][j]=mat[i][j];
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
