class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        // since we don't guarantee that the array is sorted
        // we will keep a map of the previously seen numbers

        // [key = number, value = frequency
        const map : Map<number, number> = new Map<number, number>();

        for(let i = 0; i < nums.length; i++) {
            const diff = target - nums[i];
            if(map.has(diff)) {
                return [map.get(diff), i];
            }

            map.set(nums[i], i)
        }

        return [0,0]
    }
}
