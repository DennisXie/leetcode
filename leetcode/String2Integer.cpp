#include "String2Integer.h"

using namespace std;

int String2Integer::myAtoi(string str)
{
	if (str.size() == 0) return 0;
	
	int nAns = 0;
	bool bStart = false;
	int nFlag = 1;
	string::iterator strIt = str.begin();
	while (strIt != str.end())
	{
		char ch = *strIt;
		int num = ch - '0';
		if ((num >= 0) && (num <= 9))
		{
			bStart = true;
			int tempAns = nAns * 10 + num * nFlag;
			long long test = (long long)nAns * 10 + num * nFlag;
			int nMax = 0x7fffffff, nMin = 0x80000000;
			if ((test > nMax) || (test < nMin))
			{
				if (nFlag > 0)
				{
					nAns = 2147483647;
				}
				else
				{
					nAns = -2147483648;
				}
				break;
			}
			else
			{
				nAns = tempAns;
			}
		}
		else if (ch == ' ' && !bStart)
		{

		}
		else if (ch == '-' && !bStart)
		{
			nFlag = -1;
			bStart = true;
		}
		else if (ch == '+' && !bStart)
		{
			nFlag = 1;
			bStart = true;
		}
		else if (!bStart)
		{
			nAns = 0;
			break;
		}
		else
		{
			break;
		}
		++strIt;
	}

	return nAns;
}