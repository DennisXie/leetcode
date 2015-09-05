#include "SumRoot2LeafNumbers.h"

int SumRoot2LeafNumbers::count;

int SumRoot2LeafNumbers::sumNumbers(TreeNode *root)
{
	count = 0;
	countNumber(root, 0);
	return count;
}


void SumRoot2LeafNumbers::countNumber(TreeNode *root, int n)
{
	if (root == nullptr)
	{
		return;
	}

	n = n * 10 + root->val;
	if (root->left == nullptr && root->right == nullptr)
	{
		count += n;
		return;
	}
	
	countNumber(root->left, n);
	countNumber(root->right, n);
}
