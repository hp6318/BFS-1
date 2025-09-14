# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Solution 1: BFS 
Maintain a queue to do BFS, for each level we get the size of the queue and run a FOR 
loop to do 2 things:
    1) add the nodes at current level to current level's list
    2) Add the neighbors of nodes at the current level to the queue
Time Complexity: O(N)
Space Complexity: O(N/2) = O(N), N/2 = leaf nodes for perfect binary tree. At the last level, 
                  Queue will have all the leaf nodes
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        levelOrder_list = []
        
        bfs_queue = deque() # queue for BFS traversal
        bfs_queue.append(root)

        while (len(bfs_queue)!=0):
            curr_level_nodes_size = len(bfs_queue) # total nodes at this level
            curr_level_nodes = []
            for i in range(curr_level_nodes_size):
                curr_node = bfs_queue.popleft()
                curr_level_nodes.append(curr_node.val) # add this level node to this level's list
                # Add neighbors of this node to the queue
                if curr_node.left!=None:
                    bfs_queue.append(curr_node.left)
                if curr_node.right!=None:
                    bfs_queue.append(curr_node.right)
            
            levelOrder_list.append(curr_level_nodes) # add this level's list
        
        return levelOrder_list

'''
Solution 2: DFS  with Recursion 
 - level : Parameter of recursion
    - at each node, we want to preserve the level value when recursion returns back to
      to the function call of this node. 
Final answer list's size determine if we have already created a list for storing nodes
at this level
    eg. node=3, ans = [], ans.size = 0, level = 0, no list at level 0 exits, so add a new list and add the node's val, ans = [[3]]
        node = 9, ans = [[3]], ans.size = 1, level = 1, no list at level 1 exists, so ans  so add a new list and add the node's val, ans = [[3],[9]]
        node = 20, ans [[3],[9]], ans.size = 2, level =1, as size!=level, level 1 list exists. so just update list at level=1, ans = [[3],[9,20]]
Time Complexity: O(N)
Space Complexity: O(h), h = Height of tree, recursion stack space

'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        levelOrder_list = list()

        self.helper(root,0,levelOrder_list) # curr_node, level, final answer list
        
        return levelOrder_list
    
    def helper(self,node, level, levelOrder_list):
        # base
        if node == None:
            return

        # logic
        if len(levelOrder_list)==level:
            # this level's list has yet not been created in the final answer
            levelOrder_list.append([])

        # add the curr node to it's level's list
        levelOrder_list[level].append(node.val)

        # left traversal
        self.helper(node.left,level+1,levelOrder_list)

        # right traversal
        self.helper(node.right,level+1,levelOrder_list)

