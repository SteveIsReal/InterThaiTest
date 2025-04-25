#include <stdio.h>

int main(){

    int x[3] = {0};
    for(int i=0;i<3;i++){
        scanf(" %d",&x[i]);
    }
    int result = 0;
    int len = sizeof(x) / sizeof(x[1]);
    //if you have 3 elements it will result as 12
    //cuz int is 4 bytes and 3 elements is 3*4 = 12!!!!
    //Now / by 4 will get the len of elements 12/4 is 3!
    for(int i=0;i<len;i++){
        if(result < x[i]){
            result = x[i];
        }
    }

    printf("%d",result);
    return 0;
}
