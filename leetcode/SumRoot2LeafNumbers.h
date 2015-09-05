#pragma once

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) :val(x), left(nullptr), right(nullptr){};
};

//面试中，这道题，要考虑到表达的数字如果超过范围怎么办？
class SumRoot2LeafNumbers
{
public:
	static int count;
	static int sumNumbers(TreeNode *root);
	static void countNumber(TreeNode *root, int n);
};
