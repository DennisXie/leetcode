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

//���ջ+��ջ��ʵ�ֶ���
vector<int> maxSlidingWindow2(vector<int> &nums, int k)
{
	//������ջ1��ջ2���
	//�ø���ջ����ջ1��ջ2�����ֵ��������ջ��Ϊ��ջ1�͸�ջ2.
	//�����У����ȵ���ջ2��ֵ����ջ2Ϊ�գ��Ƚ�ջ1���ε�������ջ2����ջ������Ӧ�Ĳ�����
	//��ջ1��¼���ǽ���ջ1�ĵ�ǰ���ֵ����ջ2��¼���ǽ���ջ2�ĵ�ǰ���ֵ�������ǴӸ�ջ1�л�ȡֵ����
	//�����Ϳ������һ���ܹ���O(1)��ʱ���ڻ�ȡ���ֵ�Ķ�����~
	return vector<int>();
}
