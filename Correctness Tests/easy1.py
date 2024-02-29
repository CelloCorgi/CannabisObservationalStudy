# Instructions:
# Before typing:
# 1. Open the command palette (Ctrl+shift+P on Windows, Command+Shift+P on Mac) 
#    and search for: Enable Saving Files
# 2. Hit the RUN button to open the terminal, type '../../scripts/recordTerminal.sh'
# 3. Press Ctrl+alt+R on Windows(Ctrl+Option+R on Mac) to start recording your keystrokes 
# Begin typing!

class Solution(object):
    """
    You are given a string `s` consisting of lowercase English letters. 
    A duplicate removal consists of choosing two adjacent and equal letters and removing them.
    We repeatedly make duplicate removals on `s` until we no longer can.
    Return the final string after all such duplicate removals have been made. 
    It can be proven that the answer is unique.
    """

    # Example 1:
    """
    Input: s = "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
    and this is the only possible move.  The result of this move is that the string is "aaca",
    of which only "aa" is possible, so the final string is "ca".
    """
    # Example 2:
    """
    Input: s = "azxxzy"
    Output: "ay"
    """

    # Constraints:
    """
    1 <= s.length <= 10^5
    `s` consists of lowercase English letters.
    """
    
    def removeDuplicates(self, s):
        stack = []
        answer = ''
        for letter in s:
            if len(stack):
                if stack[-1] == letter:
                    stack.pop()
                    continue
            stack.append(letter)
        for i in stack:
            answer+=i
        return answer
