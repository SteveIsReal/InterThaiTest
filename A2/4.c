#include <stdio.h>

int main(){

    int x[] = {0};
    int re;
    scanf("%d",&re);
    for(int i=0;i<re;i++){
        scanf("%d",&x[i]);
    }
    int n = sizeof(x) / sizeof(x[0]);
    for(int j=0;j<n;j++){

        printf("%d ",x[j]);
    }

    return 0;
}

