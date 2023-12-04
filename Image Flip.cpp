#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int n,m;
    cin>>n>>m;
    
    int arr[n][m],brr[n][m];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>arr[i][j];
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            brr[i][j]=arr[i][m-j-1];
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(brr[i][j]==0){
                brr[i][j]=1;
            }
            else{
                brr[i][j]=0;
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<brr[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
