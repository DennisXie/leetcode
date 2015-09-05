#include "AddBinary.h"

using namespace std;

string AddBinary::addBinary(string a, string b)
{
	string ans = "";
	if (a.length() < b.length()) a.swap(b);

	string::reverse_iterator r_ita = a.rbegin(), r_itb = b.rbegin();

	char last = '0';
	while (r_ita != a.rend())
	{
		if (r_itb != b.rend())
		{
			if (last == '0')
			{
				if (*r_ita == '1' && *r_itb == '1')
				{
					ans.insert(0, 1, '0');
					last = '1';
				}
				else if ((*r_ita == '1' && *r_itb == '0')||(*r_ita == '0' && *r_itb == '1'))
				{
					ans.insert(0, 1, '1');
				}
				else
				{
					ans.insert(0, 1, '0');
				}
			}
			else
			{
				if (*r_ita == '1' && *r_itb == '1')
				{
					ans.insert(0, 1, '1');
					last = '1';
				}
				else if ((*r_ita == '1' && *r_itb == '0') || (*r_ita == '0' && *r_itb == '1'))
				{
					ans.insert(0, 1, '0');
					last = '1';
				}
				else
				{
					ans.insert(0, 1, '1');
					last = '0';
				}
			}

			++r_ita;
			++r_itb;
		}
		else
		{
			if (last == '0')
			{
				ans.insert(0, 1, *r_ita);
			}
			else
			{
				if (*r_ita == last)
				{
					ans.insert(0, 1, '0');
				}
				else
				{
					ans.insert(0, 1, '1');
					last = '0';
				}
			}
			++r_ita;
		}
	}

	if (last == '1') ans.insert(0, 1, last);

	return ans;
}
