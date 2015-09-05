#include "ThreeSum.h"

using namespace std;

vector<vector<int>> threeSum(vector<int> &nums)
{
	vector<vector<int>> ans;
	if (nums.size() < 3) return ans;

	sort(nums.begin(), nums.end());
	int last = nums.front() + 1;


	vector<int>::iterator end = nums.end();
	--end;
	--end;
	for (vector<int>::iterator pi = nums.begin(); pi != end; ++pi)
	{
		if (*pi == last) continue;
		auto a = pi;
		++a;
		auto b = nums.end();
		--b;
		while (a != b)
		{
			if (*a + *b + *pi == 0)
			{
				ans.push_back(vector<int>({ *pi, *a, *b }));
				int lasta = *a;
				int lastb = *b;
				while (a != b && *a == lasta)
				{
					++a;
				}

				while (a != b && *b == lastb)
				{
					--b;
				}
				
				if (a == b) break;
			}
			else if (*a + *b + *pi > 0)
			{
				--b;
			}
			else if (*a + *b + *pi < 0)
			{
				++a;
			}
		}
		last = *pi;
	}
	return ans;
}


int threeSumClosest(vector<int> &nums, int target)
{
	if (nums.size() < 3) return 0;
	int minans = 0;
	
	sort(nums.begin(), nums.end());
	for (int i = 0; i < 3; ++i)
	{
		minans += nums[i];
	}

	for (int i = 0; i < nums.size(); ++i)
	{
		int j = i + 1;
		int k = nums.size() - 1;
		while (j < k)
		{
			int sum = nums[i] + nums[j] + nums[k];
			if (abs(minans - target) > abs(sum - target)) minans = sum;

			if (sum == target)
			{
				return sum;
			}
			else if (sum > target)
			{
				--k;
			}
			else
			{
				++j;
			}
		}
	}

	return minans;
}
