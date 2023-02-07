/*


Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of 
the nodes in the tree.
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


*/

// Observations : 
// 1)         1 <= K <= N
// 2)         1 <= N <= 1e4
// 3) Since we're given binary search tree
/*
                             9
                            / \
                           2  10 
                          / \ / \
                         1  7 8  11
*/
// Brute force : 
// 1) Store inorder in a vector and return ans[k-1]
//      will take T.C : O(n) -> O(k)
//                S.C : O(n) -> O(k)
// 2) Reduced S.C : O(1)
void inorder_traversal(Node *root,vector<int>&ans,int K,int &currently_returned)
{
    if(currently_returned==K)
        return ans.push_back(root->val);
    if(root==NULL)
        return;
    inorder_traversal(root->left,ans,currently_returned);
    // ans.push_back(root->val);
    inorder_traversal(root->right,ans,currently_returned);
    currently_returned++;
}
//S.C : O(1)
int solve(Node *root,int K)
{
    vector<int>ans;
    int currently_returned=0;
    inorder_traversal(root,ans,K,0);
    return ans.back();
}