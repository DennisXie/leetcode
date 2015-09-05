#include "TwoSum.h"

using namespace std;

vector<int> TwoSum::twoSum(vector<int> &nums, int target)
{
	vector<int> index;
	map<int, vector<int>::size_type> indexMap;

	for (vector<int>::size_type i = 0; i < nums.size(); ++i)
	{
		if (indexMap.find(nums[i]) == indexMap.end())
		{
			indexMap.insert(make_pair(nums[i], i + 1));
		}

		if ((indexMap.find(target - nums[i]) != indexMap.end()) && (indexMap.find(target - nums[i])->second != (i + 1)))
		{
			index.push_back(indexMap.find(target - nums[i])->second);
			index.push_back(i + 1);
			return index;
		}
	}
}