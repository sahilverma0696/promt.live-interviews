
/*

There is an undirected connected tree with n nodes labeled from 0 to n - 1 
and n - 1 edges.


You are given the integer n and the array edges where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the 
distances between the ith node in the tree and all other nodes.


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

*/


//Observations : 
// 1) answer[i] = sum of distances from ith node to all other nodes
/*
                1                           ->              0
               / \                          
              2   3                         ->              1
             / \ / \
            4  5 6  7                       ->              2
    
    ans[1] = dist(1,2)+dist(1,3)+dist(1,4)+dist(1,5)+dist(1,6)+dist(1,7) =
     0 + 2*1 + 4*2 = 10
    //DFS at 1 => 1,2,3,4,5,6,7
    //DFS at 2 => 1,2,3,4,5,6,7
    //...
    //...
    //DFS at nth node => 1,2,3,4,5,6,7

*/
// Approaches : 
// 1) DFS at every node and take depth of all other nodes
//          O(n^2) TC and SC O(n)
// 2) n <= 3e4 -> TLE
//      O(3e4*3e4)=O(9e8)
//      In 1 sec we expect ~O(2e8)


/*
                1                           ->              0
               / \                          
              2   3                         ->              1
             / \ / \
            4  5 6  7 

            // A -> B -> C
            //dist(A,C) = known
            //dist(A,B) = known
            //dist(B,C) = dist(A,C)-dist(A,B)

              2                       
             / \ 
            4   5 


            [2,4,5] [1,3,6,7]

    ans[1] = [0,1,1,2,2,2,2]
    ans[2] = [1,0,2,1,1,3,3]
    ans[3] = [1,2,0,3,3,1,1]
*/

//TC is O(n) and SC is O(4*n)=O(n)
void dfs(int node,vector<vector<int>>&adj,vector<int>&visited,
            vector<int>&depth,vector<int>&subtree_size)
{
    visited[node]++;
    subtree_size[node]=1;
    for(auto i:adj[node])
        if(!visited[i])
        {
            depth[i]=depth[node]+1;
            dfs(i,adj,visited,depth,subtree_size);
            subtree_size[node]+=subtree_size[i];
        }
}
void dfs2(int node,vector<vector<int>>&adj,vector<int>&visited,
            vector<int>&subtree_size,vector<int>&answer)
{
    visited[node]++;
    for(auto i:adj[node])
        if(!visited[i])
        {
            int n=adj.size();
            int parent_answer=ans[node];
            int current_answer=parent_answer;
            current_answer += (n-2*subtree_size[i]);
            answer[i]=current_answer;
            dfs2(i,adj,visited,subtree_size,answer);
        }
}
vector<long long> solve(int n,vector<pair<int,int>>&edges)
{
    //modes : 0 to n-1
    vector<vector<int>>adj(n);  //O(n)
    //making a graph
    for(auto [i,j]:edges)
        adj[i].push_back(j),
        adj[j].push_back(i);
    vector<int>visited(n); //O(n)
    vector<int>depth(n);    //O(n)
    vector<int>subtree_size(n); //O(n)
    //running a dfs to get parent's answer
    dfs(0,adj,visited,depth,subtree_size);
    vector<long long>answer(n);
    ans[0]=accumulate(depth.begin(),depth.end(),0LL); //sum up all values inside depth vector
    visited.clear();
    dfs2(0,adj,visited,subtree_size,answer);
    return answer;
}