#ifndef NUMBEROF1BITS_H
#define NUMBEROF1BITS_H
#pragma once

typedef unsigned int uint32_t;

class NumberOf1Bits
{
public:
	int hammingWeight(uint32_t n)
	{
		uint32_t flag = 1;
		uint32_t count = 0;
		while (flag)
		{
			if (n & flag) ++count;
			flag = flag << 1;
		}

		return count;
	}
};

#endif