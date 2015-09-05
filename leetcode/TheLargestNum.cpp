#include "TheLargestNum.h"
#include <algorithm>

using namespace std;

string TheLargestNum::largest(vector<int> &nums)
{
	auto fn = [](int a, int b)
		{
			char num1[50], num2[50];
			sprintf(num1, "%d%d", a, b);
			sprintf(num2, "%d%d", b, a);

			for (size_t i = 0; i < strlen(num1); ++i)
			{
				if (num1[i] > num2[i])
					return false;
				else if (num1[i] < num2[i])
					return true;
			}
			return false;
		};

	sort(nums.begin(), nums.end(), fn);
	
	char num[100];
	string ans;
	//if the nums = {0,0, 0, 0, 0}
	for (vector<int>::value_type i : nums)
	{
		if (i != 0 || ans != "")
		{
			sprintf(num, "%d", i);
			ans.append(num);
		}
	}

	if (ans == "")
	{
		ans = "0";
	}

	return ans;
}


bool TheLargestNum::smaller(int a, int b)
{
	char num1[50], num2[50];
	sprintf(num1, "%d%d", a, b);
	sprintf(num2, "%d%d", b, a);

	for (size_t i = 0; i < strlen(num1); ++i)
	{
		if (num1[i] > num2[i])
			return false;
		else if (num1[i] < num2[i])
			return true;
	}
	return false;
}
