#include <stdlib.h>
#include "DivideTwoIntegers.h"

int uintlen(unsigned int a)
{
	int len = 0;
	while (a > 0)
	{
		++len;
		a = a / 10;
	}

	return len;
}

int divide(int dividend, int divisor)
{
	int end_flag = 1;
	int sor_flag = 1;

	//The flag;
	if (dividend < 0)
	{
		end_flag = -1;
	}
	else if (dividend == 0)
	{
		return 0;
	}

	if (divisor < 0)
	{
		sor_flag = -1;
	}

	//if the dividend < 0 then we take the opposite num.
	unsigned int udividend = (end_flag == 1 || dividend == INT_MIN) ? dividend : -dividend;
	unsigned int udivisor = (sor_flag == 1 || divisor == INT_MIN) ? divisor : -divisor;

	//Find the length of dividend and divisor.
	int lenend = uintlen(udividend);
	int lensor = uintlen(udivisor);

	if (udividend < udivisor) return 0;

	unsigned int ans = 0;
	unsigned int base = 1;
	unsigned int i = 0;
	//Calculate the base.
	for (i = 0; i < lenend - lensor; ++i)
		base *= 10;

	//Calculate the answer.
	for (i = base; i > 0; i /= 10)
	{
		unsigned int temp = 0;
		unsigned int temp_divisor = 0;
		//udivisor * i may be overflow.
		if (udivisor * i / i != udivisor)
		{
			temp_divisor = UINT_MAX;
		}
		else
		{
			temp_divisor = udivisor * i;
		}
		while (udividend >= temp_divisor)
		{
			++temp;
			udividend -= temp_divisor;
		}

		ans = ans * 10 + temp;
	}

	if (ans > INT_MAX && end_flag < 0 && sor_flag < 0) return INT_MAX;

	if (end_flag != sor_flag)
		return (int)ans * -1;
	else
		return (int)ans;
}