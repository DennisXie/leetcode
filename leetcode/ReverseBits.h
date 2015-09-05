#ifndef REVERSEBITS_H
#define REVERSEBITS_H
#pragma once

typedef unsigned int uint32_t;

class ReverseBits
{
public:
	static uint32_t reverseBits(uint32_t n)
	{
		uint32_t flag = 1;
		uint32_t ans = 0;

		while (flag)
		{
			if (n & flag)
			{
				ans = (ans << 1) + 1;
			}
			else
			{
				ans = ans << 1;
			}

			flag <<= 1;
		}

		return ans;
	}
};

#endif