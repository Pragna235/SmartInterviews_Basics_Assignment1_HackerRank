//n a given integer N, check whether the ith bit is set or not.
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,i;
    cin>>n>>i;
    if(n&(1<<i))
        cout<<"true";
    else
        cout<<"false";
    return 0;
}

