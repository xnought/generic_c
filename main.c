#include <stdio.h>

int factorial(int n)
{
	return n <= 1 ? 1 : n * factorial(n - 1);
}

int main()
{

	int n = 5;
	printf("factorial(%d) = %d", n, factorial(n));

	return 0;
}