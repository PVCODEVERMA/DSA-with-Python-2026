class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # If array has only one element
        if n == 1:
            return 0

        # If first element is 0, we can't move
        if arr[0] == 0:
            return -1

        maxReach = arr[0]
        steps = arr[0]
        jumps = 1

        for i in range(1, n):
            # If we reached the end
            if i == n - 1:
                return jumps

            # Update maxReach
            maxReach = max(maxReach, i + arr[i])

            steps -= 1

            # If no more steps left
            if steps == 0:
                jumps += 1

                # If current index is beyond maxReach
                if i >= maxReach:
                    return -1

                # Reinitialize steps
                steps = maxReach - i

        return -1
