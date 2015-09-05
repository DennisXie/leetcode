#include "houserobber.h"

using namespace std;

int HouseRobber::rob(vector<int> &nums)
{
	int n = nums.size();
	try
	{
		vector<int> cash(n + 1, 0);
		cash.at(1) = nums.at(0);

		for (int i = 2; i <= n; ++i)
		{
			for (int j = i - 2; j >= 0; --j)
			{
				int temp = nums[i - 1] + cash[j];
				if (temp > cash[i]) cash[i] = temp;
			}
		}
		
		int nMaxCash = cash.at(n) > cash.at(n - 1) ? cash.at(n) : cash.at(n - 1);
		return nMaxCash;
	}
	catch (exception e)
	{
		return 0;
	}
}