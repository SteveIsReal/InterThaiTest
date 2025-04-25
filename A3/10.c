#include <stdio.h>

int main(){

    int x[3] = {0};
    int count = 0;
    int position = 1;
    scanf("%d %d %d",&x[0],&x[1],&x[2]);

    do{
        if(position + x[1] <= x[0]){
            position += x[1];
        }
        else{
            position = (position + x[1]) - x[0];
        }
        count++;

    }while(position != 1 && position != x[2]);

    if(position == x[2]){count++;}

    printf("%d\n",count);
    return 0;
}
