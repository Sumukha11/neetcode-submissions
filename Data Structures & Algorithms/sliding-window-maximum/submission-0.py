from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        dq = deque()
        result = []

        for right in range(len(nums)):

            # Remove indices outside the window
            if dq and dq[0] < right - k + 1:
                dq.popleft()

            # Remove smaller candidates from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Record maximum once window is full
            if right >= k - 1:
                result.append(nums[dq[0]])

        return(result)