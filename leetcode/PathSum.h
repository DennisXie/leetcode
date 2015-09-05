#pragma once

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) :val(x), left(nullptr), right(nullptr){};
};


class PathSum
{
public:
	bool hasPathSum(TreeNode *root, int sum);
};
