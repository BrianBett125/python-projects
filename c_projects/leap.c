#include <stdio.h>
/**
 * main - entry point of the program
 * description: a program to determine if a year
 * is a leap year
 *
 * Return: always (0) success
 */
int main(void)
{
	int year;

	printf("enter the year: \n");
	scanf("%d", &year);
	if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
	{
		printf("%d is a leap year\n", year);
	}
	else
	{
		printf("%d is not a leap year", year);
	}
	return (0);
}
