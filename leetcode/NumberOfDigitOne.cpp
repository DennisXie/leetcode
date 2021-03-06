#include <cstdio>
#include <cstdlib>
#include <cstring>
#include "NumberOfDigitOne.h"

int NumberOfDigitOne::countDigitOne(int n)
{
	if (n <= 0) return 0;

	char strN[20];
	memset(strN, 0, 20);
	sprintf(strN, "%d", n);

	return NumberOf1(strN);
}

int NumberOfDigitOne::NumberOf1(const char *strN)
{
	if (!strN || *strN < '0' || *strN > '9' || *strN == '\0') return 0;

	int first = *strN - '0';
	unsigned int length = static_cast<unsigned int>(strlen(strN));

	if (length == 1 && first == 0)	return 0;
	if (length == 1 && first > 0)	return 1;

	int numFirstDigit = 0;
	if (first > 1)
		numFirstDigit = PowerBase10(length - 1);
	else if (first == 1)
		numFirstDigit = atoi(strN + 1) + 1;

	int numOtherDigits = first * (length - 1) * PowerBase10(length - 2);
	int numRecursive = NumberOf1(strN + 1);

	return numFirstDigit + numOtherDigits + numRecursive;
}

int NumberOfDigitOne::PowerBase10(unsigned int n)
{
	int result = 1;
	for (unsigned int i = 0; i < n; ++i)
		result = result * 10;
	return result;
}