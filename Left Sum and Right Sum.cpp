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
    
    int arr[n],ls[n],rs[n], brr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    ls[0]=0;
    rs[n-1]=0;
    
    for(int i=1;i<n;i++){
        ls[i]=ls[i-1]+arr[i-1];
    }
    
    for(int i=n-2;i>=0;i--){
        rs[i]=rs[i+1]+arr[i+1];
    }
    
    for(int i=0;i<n;i++){
        brr[i]=abs(ls[i]-rs[i]);
        //cout<<"ls = "<<ls[i]<<" rs = "<<rs[i]<<endl;
        cout<<brr[i]<<" ";
    }
    cout<<endl;
    
    return 0;
}
