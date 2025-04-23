#include <stdio.h>

int main()
{
	char c[100],v[100];
	scanf("%s",&c);
	scanf("%s",&v);
	printf("Hello %s %s",c,v);
	char z[3];
	z[0] = c[0];
	z[1] = c[1];
	z[2] = '\0';
	char x[3];
	x[0] = v[0];
	x[1] = v[1];
	x[2] = '\0';
	printf("\n%s%s",z,x);
	return 0;
}
