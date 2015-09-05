#include "BinaryTreeTraversal.h"

using namespace std;

vector<int> postorderTraversal(TreeNode *root)
{
    vector<int> ans;
    stack<StackSlot> travelStack;

    if (root == nullptr) return ans;

    TreeNode *pnode = root;

    while (pnode || !travelStack.empty())
    {
        if (pnode != nullptr)
        {
            if (pnode->left != nullptr)
            {
                StackSlot slot(pnode, true);
                travelStack.push(slot);
                pnode = pnode->left;
            }
            else
            {
                StackSlot slot(pnode, false);
                travelStack.push(slot);
                pnode = pnode->right;
            }
        }
        else
        {
            StackSlot &slot = travelStack.top();
            if (slot.goRight)
            {
                slot.goRight = false;
                pnode = slot.node->right;
             }
             else
             {
                ans.push_back(slot.node->val);
                pnode = nullptr;
                travelStack.pop();
             }
         }
    }

    return ans;
}


vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> ans;
    stack<TreeNode *> travelStack;

    TreeNode *pnode = root;

    while (pnode || !travelStack.empty())
    {
        if (pnode != nullptr && pnode->left != nullptr)
        {
            travelStack.push(pnode);
            pnode = pnode->left;
            continue;
        }
        else if (pnode != nullptr && pnode->left == nullptr)
        {
        }
        else if (pnode == nullptr)
        {
            pnode = travelStack.top();
            travelStack.pop();
        }

        ans.push_back(pnode->val);
        pnode = pnode->right;
    }

    return ans;
}


vector<int> preorderTraversal(TreeNode *root)
{
    vector<int> ans;
    stack<TreeNode *> travelStack;

    TreeNode *pnode = root;

    while (!travelStack.empty() || pnode != nullptr)
    {
        if (pnode != nullptr)
        {
            ans.push_back(pnode->val);
            travelStack.push(pnode);
            pnode = pnode->left;
        }
        else
        {
            pnode = travelStack.top();
            travelStack.pop();
            pnode = pnode->right;
        }
    }

    return ans;
}
