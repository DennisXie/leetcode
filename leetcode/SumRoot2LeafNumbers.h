#pragma once

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) :val(x), left(nullptr), right(nullptr){};
};

//�����У�����⣬Ҫ���ǵ������������������Χ��ô�죿
class SumRoot2LeafNumbers
{
public:
	static int count;
	static int sumNumbers(TreeNode *root);
	static void countNumber(TreeNode *root, int n);
};
