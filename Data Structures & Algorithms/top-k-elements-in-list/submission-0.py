class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a freq. map to find how many times a number is present in the array. 

        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        # now that we know how many times each number occurs, we want to put those numbers in order
        sorted_keys = sorted(freqMap, key = lambda x: freqMap[x], reverse=True)
        return sorted_keys[:k]

        