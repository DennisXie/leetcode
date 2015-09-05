#pragma once
#include <algorithm>
struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) :val(x), left(nullptr), right(nullptr) {};
};

class InvertBinaryTree
{
public:
	static TreeNode *invertTree(TreeNode *root);
	static void revert(TreeNode **proot);
};