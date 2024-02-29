
class Solution(object):
    """
    Given the root of a binary tree, return all root-to-leaf paths in given format.
    You can return the paths in any order.
    A leaf is a node with no children.
    """

    # Example 1:
    """
            [1]
          /     \
         /       \
       [2]       [3]
         \
          \
          [5]
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]
    """
    # Example 2:
    """
    Input: root = [1] 
    Output: ["1"]
    """

    #Constraints:
    """
    The number of nodes in the tree is in the range [1,100].
    -100 <= Node.val <= 100
    """

    #Definition for a binary tree node.
    """
    class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    """

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []        
        def path(root, s):            
            if not root.left and not root.right:
                ans.append(s)            
            if root.left:
                path(root.left,s+"->"+str(root.left.val))
            if root.right:
                path(root.right,s+"->"+str(root.right.val))           
        path(root, str(root.val))
        return ans
    
    