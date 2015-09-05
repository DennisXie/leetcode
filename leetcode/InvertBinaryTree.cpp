#include "InvertBinaryTree.h"

TreeNode *InvertBinaryTree::invertTree(TreeNode *root)
{
	revert(&root);
	return root;
}


void InvertBinaryTree::revert(TreeNode **proot)
{
	if (*proot == nullptr) return;

	revert(&((*proot)->left));
	revert(&((*proot)->right));

	TreeNode *temp = nullptr;
	temp = (*proot)->left;
	(*proot)->left = (*proot)->right;
	(*proot)->right = temp;
}