#include <stdio.h>

int main(){
    
    int x;
    int result[4] = {0};
    scanf("%d",&x);

    while(x>0){
        if(x-10 >= 0){
            result[0]++;
            x -= 10;
        }
        else if(x-5 >= 0){
            result[1]++;
            x -= 5;
        }
        else if(x-2 >= 0){
            result[2]++;
            x -= 2;

        }
        else{
            result[3]++;
            x -= 1;
        }

    }

    printf("10 = %d\n5 = %d\n2 = %d\n1 = %d",result[0],result[1],result[2],result[3]);
    return 0;

}
