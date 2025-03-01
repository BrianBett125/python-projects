#include <stdio.h>
/**
 * main - entry point of the program
 * description: displays a list of even numbers in C
 *
 * Return: always (0) success
 */
int main(void)
{
	int limit, i;

	printf("enter the limit: ");
	scanf("%d", &limit);
	printf("the even numbers upto %d are\n", limit);
	for (i = 2; i <= limit; i += 2)
	{
		printf("%d", i);
	}
	printf("\n");
	return (0);
}
