#include <stdio.h>
/**
 * main - entry point of the program
 * description: a program to compare two numbers using else if
 *
 * Return: always (0) success
 */
int main(void)
{
	int num1, num2;

	printf("enter the first number\n");
	scanf("%d", &num1);
	printf("enter the second number\n");
	scanf("%d", &num2);
	if (num1 == num2)
	{
		printf("both numbers are equal\n");
	}
	else if (num1 > num2)
	{
		printf("the larger number is %d\n", num1);
		printf("the lesser number is %d\n", num2);
	}
	else
	{
		/*num1 < num2*/
		printf("the larger number is %d\n", num2);
		printf("the smaller number is %d\n", num1);
	}
	return (0);
}

