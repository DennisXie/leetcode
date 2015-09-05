#include "MajorityElement.h"

using namespace std;

int MajorityElement::majorityElement(vector<int> &nums)
{
	int count = 0;
	int number = nums.front();
	for (const vector<int>::value_type &i : nums)
	{
		if (count == 0)
		{
			number = i;
		}

		if (i == number)
			++count;
		else
			--count;
	}

	return number;
}


vector<int> MajorityElement::majorityElement2(vector<int> &nums)
{
	int m, n, cm, cn;
	m = n = cm = cn = 0;
	for (const vector<int>::value_type &i : nums)
	{
		if (m == i)
		{
			++cm;
		}
		else if (n == i)
		{
			++cn;
		}
		else if (cm == 0)
		{
			++cm;
			m = i;
		}
		else if (cn == 0)
		{
			++cn;
			n = i;
		}
		else
		{
			--cm;
			--cn;
		}
	}

	cm = cn = 0;
	for (const vector<int>::value_type &i : nums)
	{
		if (m == i)
		{
			++cm;
		}
		else if (n == i)
		{
			++cn;
		}
	}

	vector<int> ans;
	if (cm > static_cast<int>(nums.size() / 3)) ans.push_back(m);
	if (cn > static_cast<int>(nums.size() / 3)) ans.push_back(n);
	return ans;
}
