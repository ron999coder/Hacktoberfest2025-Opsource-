class Solution(object):
    def combinationSum(self, candidates, target):
        
        res = []

        def backtrack(start, path, total):
            # Base case: if sum equals target → valid combination
            if total == target:
                res.append(list(path))
                return
            # If sum exceeds target → stop exploring
            if total > target:
                return

            # Explore from 'start' to allow reuse of same element
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i+1 because we can reuse
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res
