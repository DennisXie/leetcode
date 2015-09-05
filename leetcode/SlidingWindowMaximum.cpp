#include "SlidingWindowMaximum.h"

using namespace std;

vector<int> maxSlidingWindow(vector<int> &nums, int k)
{
	deque<int> maxdeque;
	vector<int> ans;

	if (!nums.empty()) maxdeque.push_back(nums[0]);
	for (size_t i = 1; i < k; ++i)
	{
		while (!maxdeque.empty() && maxdeque.back() < nums[i])
			maxdeque.pop_back();
		maxdeque.push_back(nums[i]);
	}

	//We need to consider the condition the the max deque is empty.
	if (!nums.empty()) ans.push_back(maxdeque.front());

	for (size_t i = k; i < nums.size(); ++i)
	{
		if (nums[i - k] == maxdeque.front()) maxdeque.pop_front();
		while (!maxdeque.empty() && maxdeque.back() < nums[i])
			maxdeque.pop_back();
		maxdeque.push_back(nums[i]);
		ans.push_back(maxdeque.front());
	}

	return ans;
}

//最大栈+用栈来实现队列
vector<int> maxSlidingWindow2(vector<int> &nums, int k)
{
	//队列有栈1和栈2组成
	//用辅助栈保存栈1和栈2的最大值，这两个栈记为辅栈1和辅栈2.
	//队列中，优先弹出栈2的值，如栈2为空，先将栈1依次弹出并入栈2，辅栈进行相应的操作。
	//辅栈1记录的是进入栈1的当前最大值，辅栈2记录的是进入栈2的当前最大值（而不是从辅栈1中获取值）。
	//这样就可以组成一个能够在O(1)的时间内获取最大值的队列了~
	return vector<int>();
}
