#include <stdio.h>

	float float_fact(float n)
	{
		return n <= 1 ? 1 : n * float_fact(n - 1);
	}
	int int_fact(int n)
	{
		return n <= 1 ? 1 : n * int_fact(n - 1);
	}
	long long_fact(long n)
	{
		return n <= 1 ? 1 : n * long_fact(n - 1);
	}

int main()
{

	int n = 5;
	printf("factorial(%d) = %d\n", n, int_fact(n));

	float b = 5;
	printf("factorial(%f) = %f\n", b, float_fact(b));

	long c = 5;
	printf("factorial(%ld) = %ld\n", c, long_fact(c));

	return 0;
}