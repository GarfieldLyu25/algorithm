class Solution {
    public int findDuplicate(int[] nums) {
        //找环的入口
        int slow = nums[0], fast = nums[nums[0]];
        while(nums[slow] != nums[fast]){
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        fast = 0;
        while(nums[fast] != nums[slow]){
            slow = nums[slow];
            fast = nums[fast];
        }
        return nums[slow];
    }
}