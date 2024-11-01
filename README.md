Generic copy and paste mechanism for C. Yeah I know you can do this with macros, but I wanted to see what I could implement quickly.

```c
#include <stdio.h>

COPY factorial T F
	T F(T n)
	{
		return n <= 1 ? 1 : n * F(n - 1);
	}
COPY_END
	
PASTE
	factorial float float_fact
	factorial int int_fact
	factorial long long_fact
PASTE_END


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
```

**RUN Compiler**

```bash
python3 compiler.py main.gc generic.c # convert .gc to .c
gcc generic.c && ./a.out # compile .c
```

which outputs

```
factorial(5) = 120
factorial(5.000000) = 120.000000
factorial(5) = 120
```
