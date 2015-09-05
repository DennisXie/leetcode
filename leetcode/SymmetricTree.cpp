#include "SymmetricTree.h"

using namespace std;

bool isSymmetric(TreeNode *root)
{
	if (root == nullptr) return true;

	deque<TreeNode *> que;
	que.push_back(root);

	deque<TreeNode *>::size_type idx = 0;
	while (idx < que.size())
	{
		TreeNode *pnode = que[idx];
		if (pnode != nullptr)
		{
			que.push_back(pnode->left);
			que.push_back(pnode->right);
		}
		++idx;
	}

	size_t count = 2;
	idx = 1;
	while (count != 0)
	{
		size_t nextCount = 0;
		for (size_t i = 0; i < count; ++i)
		{
			TreeNode *pnode = que[idx + i];
			if (pnode == nullptr)
			{
				++nextCount;
			}
		}

		nextCount = 2 * count - nextCount * 2;

		size_t i = idx; size_t j = idx + count - 1;
		TreeNode *left = nullptr;
		TreeNode *right = nullptr;
		while (i < j)
		{
			left = que[i];
			right = que[j];
			if (left != nullptr && right != nullptr)
			{
				if (left->val != right->val) return false;
			}
			else
			{
				//Both of them should be nullptr.
				if (left != right) return false;
			}
			++i;
			--j;
		}

		idx = idx + count;
		count = nextCount;
	}

	return true;
}
