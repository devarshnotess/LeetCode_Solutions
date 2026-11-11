/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root){
            return 0; // Base case if the root is NUll then the depth is zero
        }
        // If the root is not null then we just check the left subtree and right subtree and then take their depths and take the maximum of them
        
        return 1 + max(maxDepth(root-> left), maxDepth(root -> right)); 
        
    }
};