//Print right-angled triangle pattern using integers. See example for more details.
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,p=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            printf("%d ",p+1);
            p=p+1;

        }
        printf("\n");
    }
    return 0;
}

