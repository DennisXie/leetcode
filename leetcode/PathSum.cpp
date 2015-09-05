#include "PathSum.h"

bool PathSum::hasPathSum(TreeNode *root, int sum)
{
	if (root == nullptr) return false;

	if (root->left == nullptr && root->right == nullptr && sum - root->val == 0) return true;
	if (hasPathSum(root->left, sum - root->val)) return true;
	if (hasPathSum(root->right, sum - root->val)) return true;
	return false;
}
