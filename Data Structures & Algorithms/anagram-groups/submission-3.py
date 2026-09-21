class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            # sort word and check if already in map, otherwise, create a new array entry to map
            sortedStr = ''.join(sorted(str))
            if map.get(sortedStr):
                map[sortedStr].append(str)
            else:
                arr = [str]
                map[sortedStr] = arr

        list = []
        for key in map.keys():
            list.append(map[key])


        return list