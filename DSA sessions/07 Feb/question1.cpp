
/*
struct Node {
    Node* left,right;
    int val;
}
Given the root of a binary tree, return the inorder traversal of its
 nodes' values.
*/
 // Observations : 
 // 1) Root can be null. 
 // 2) Node values = distinct 
 // 3) Number of nodes = N <= 500
 // 4) [In]order traversal : The value of a node is b/w the left and right child
 // -> Estimated time complexities : O(n*n) : O(n*logn) : O(n) 

 // Obs P2 :
 // 1)  () => [empty array]
 // 2)   1 => [1]
 // 3)                                  1
 /*                                    / \
                                      2   3

 */
 // [2,1,3]

 // Solution 1 : 
 // 1) Base condition : root==nullptr return;
 // 2) Recursive condition : discover_left_child -> put current node's value 
 //    inside arr -> discover right child
 //    S.C : O(n)
 //    T.C : O(n)
 void inorder_traversal(Node *root,vector<int>&ans)
 {
    if(root==NULL)
        return;
    //[2,1,3]
    inorder_traversal(root->left,ans);
    ans.push_back(root->val);
    inorder_traversal(root->right,ans);
 }
 vector<int> solve(Node *root)
 {
    vector<int> ans;
    inorder_traversal(root,ans);
    return ans;
 }





 
