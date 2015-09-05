#include <deque>
#include "PalindromeNumber.h"

using namespace std;

bool PalindromeNumber::isPalindrome(int x)
{
	deque<int> numQue;
	int div = x, mod = 0;
	while (div)
	{
		mod = div % 10;
		div = div / 10;
		numQue.push_front(mod);
	}

	deque<int>::iterator fIt = numQue.begin();
	deque<int>::reverse_iterator rIt = numQue.rbegin();
	while (rIt != numQue.rend())
	{
		if (*fIt == *rIt)
		{
			++fIt;
			++rIt;
		}
		else
		{
			return false;
		}
	}

	return true;
}