class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            bs[c].append(n)
        res = []
        for i in range(len(bs) - 1 , 0 ,-1):
            for x in bs[i]:
                res.append(x)
                if len(res) == k:
                    return res


