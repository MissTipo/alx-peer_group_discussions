#include <stdio.h>
#include <math.h>


int power(int base, int exp)
{
	int power = 1, i = 1;

	for (i = 1; i <= exp; i++)
	{
		power = power * base;
	}
	return (power);
}

int main()
{
	printf("%d\n", power(2, 4));
	printf("%f\n", pow(2, 4));

	printf("%d\n", power(2, -4));
	printf("%f\n", pow(2, -4));

	printf("%d\n", power(2, 0));
	printf("%f\n", pow(2, 0));
}

