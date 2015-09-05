#ifndef REVERSEINTEGER_H
#define REVERSEINTEGER_H
#pragma once

class ReverseInteger
{
public:
	static int reverse(int x)
	{
		int neg = -1 * 2147483647;
		int pos = 2147483647;
		int ans = 0;
		int cur = 0;
		long long big = 0;
		int mod, div = x;
		while (div)
		{
			mod = div % 10;
			cur = ans * 10 + mod;
			big = (long long)ans * 10 + mod;
			if (((x < 0) && (big < neg)) || ((x > 0) && (big > pos))) return 0;
			ans = cur;
			div = div / 10;
		}

		return ans;
	}
};

#endif