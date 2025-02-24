#include <stdio.h>
/**
 * main - entry point of the program
 * description: finds the factorial of a iven number in C
 *
 * Return: always (0) sucess
 */
int main(void)
{
	int num;
	int i;
	unsigned long long factorial = 1;

	printf("enter a non negative integer: ");
	scanf("%d", &num);

	if (num < 0)
	{
		printf("factorial is not defined for negative numbers\n");
	}
	else if (num == 0)
	{
		printf("the factorial of 0 is 1\n");
	}
	else
	{
		for (i = 1; i <= num; i++)
		{
			factorial *= i;
		}
		printf("the factorial of %d is %llu", num, factorial);
	}
	return (0);
}
