from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}          # stores frequency of characters
        q = deque()        # stores indices of characters

        for i in range(len(s)):
            # if character appears first time → push index
            if s[i] not in freq:
                q.append(i)

            # update frequency
            freq[s[i]] = freq.get(s[i], 0) + 1

            # remove non-unique characters from front
            while q and freq[s[q[0]]] > 1:
                q.popleft()

        # if queue empty → no unique character
        return -1 if not q else q[0]
