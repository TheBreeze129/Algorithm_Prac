#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int  ncow, ncandy, i, j;
	long long* cow, * candy;
	scanf("%d %d", &ncow, &ncandy);
	cow = (long long*)malloc(sizeof(long long) * ncow);
	candy = (long long*)malloc(sizeof(long long) * ncandy);
	for (i = 0; i < ncow; i++)
	{
		scanf("%lld", &(cow[i]));
	}
	for (i = 0; i < ncandy; i++)
	{
		scanf("%lld", &(candy[i]));
	}

	for (i = 0; i < ncandy; i++)
	{
		long long base = 1, temp = 0;
		for (j = 0; j < ncow; j++)
		{
			if (base > candy[i])  break;
			if (cow[j] >= base)
			{
				temp = (cow[j] < candy[i]) ? (cow[j] - base + 1) : (candy[i] - base + 1);
				base = cow[j] + 1;
				cow[j] += temp;
			}
		}
	}
	for (i = 0; i < ncow; i++) printf("%lld\n", cow[i]);
	free(cow);
	free(candy);
	return 0;
}