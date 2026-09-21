class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            # sort word and check if already in map, otherwise, create a new array entry to map
            sortedStr = ''.join(sorted(str))
            if sortedStr in map:
                map[sortedStr].append(str)
            else:
                map[sortedStr] = [str]

        list = []
        for key in map.keys():
            list.append(map[key])


        return list