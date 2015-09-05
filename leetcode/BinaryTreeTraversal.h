#pragma once
#include <vector>
#include <stack>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){};
};

struct StackSlot
{
    TreeNode *node;
    bool goRight;
    StackSlot(TreeNode *root, bool right) : node(root), goRight(right){};
};

std::vector<int> postorderTravalsal(TreeNode *root);

std::vector<int> inorderTraversal(TreeNode *root);

std::vector<int> preorderTraversal(TreeNode *root);
