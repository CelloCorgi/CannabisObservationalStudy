# Instructions:
# Before typing:
# 1. Open the command palette (Ctrl+shift+P on Windows, Command+Shift+P on Mac) 
#    and search for: Enable Saving Files
# 2. Hit the RUN button to open the terminal, type '../../scripts/recordTerminal.sh'
# 3. Press Ctrl+alt+R on Windows(Ctrl+Option+R on Mac) to start recording your keystrokes 
# Begin typing!

class Solution(object):
    """
    Given an array of distinct integers `arr`, find all pairs of 
    elements with the minimum absolute difference of any two elements.
    Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    - a, b are from `arr`
    - a < b
    - b - a equals to the minimum absolute difference of any two elements in `arr`
    """
    # Example 1:
    """
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. 
    List all pairs with difference equal to 1 in ascending order.
    """
    # Example 2:
    """
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]
    """
    # Example 3:
    """
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]
    """
    # Constraints:
    """
    - 2 <= arr.length <= 10^5
    - -10^6 <= arr[i] <= 10^6
    """
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_dif=arr[1]-arr[0]
        res=[[arr[0],arr[1]]]
    
        for i in range(1,len(arr)-1):
            q=[]
            if((arr[i+1]-arr[i])<min_dif):
                min_dif=arr[i+1]-arr[i]
                res=[]
            if(arr[i+1]-arr[i]==min_dif):
                q=[arr[i],arr[i+1]]
                res.append(q)
        return res   