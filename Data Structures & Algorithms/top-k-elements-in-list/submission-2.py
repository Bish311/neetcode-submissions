class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        res = []    
        for n, c in count.items():
            bs[c].append(n)
        for i in range(len(nums) , 0 ,-1):
            res.extend(bs[i])
            if len(res) == k:
                return res


