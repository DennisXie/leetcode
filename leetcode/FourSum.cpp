#include "FourSum.h"

using namespace std;

vector<vector<int>> fourSum(vector<int> &nums, int target)
{
	vector<vector<int>> ans;

	if (nums.size() < 4) return ans;

	sort(nums.begin(), nums.end());

	int lasti = ~nums[0];
	int lastj = ~nums[1];

	for (int i = 0; i < static_cast<int>(nums.size()) - 1; ++i)
	{
		if (nums[i] == lasti) continue;
		lasti = nums[i];

		for (int j = i + 1; j < static_cast<int>(nums.size()); ++j)
		{
			if (nums[j] == lastj && j != i + 1) continue;
			lastj = nums[j];
			
			int k = j + 1;
			int l = nums.size() - 1;
			while (k < l)
			{
				int sum = nums[i] + nums[j] + nums[k] + nums[l];
				if (sum == target)
				{
					ans.push_back(vector<int>({nums[i], nums[j], nums[k], nums[l]}));
					int lastk = nums[k];
					int lastl = nums[l];
					--l;
					++k;
					while (k < l && lastk == nums[k]) ++k;
					while (k < l && lastl == nums[l]) --l;
				}
				else if (sum > target)
				{
					--l;
				}
				else
				{
					++k;
				}
			}
		}
	}

	return ans;
}
