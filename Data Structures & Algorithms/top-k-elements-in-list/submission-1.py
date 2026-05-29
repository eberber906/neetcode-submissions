class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        data = []
        for num, cnt in counter.items():
            data.append([cnt, num])
        data.sort()
        result = []

        for i in range(k):
            result.append(data.pop()[1])

        return result
