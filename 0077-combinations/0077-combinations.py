class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(start, curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            for i in range(start, n + 1):
                curr.append(i)
                dfs(i + 1, curr)
                curr.pop()
            
        dfs(1, [])
        return ans