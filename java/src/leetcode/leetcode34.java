class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = lowerBound(nums, target);
        if( l == nums.length || nums[l] != target){
            return new int[]{-1, -1};
        }
        int r = lowerBound(nums,target + 1) - 1;
        return new int[]{l,r};
    }
    private int lowerBound(int[] nums, int target){
        int left = 0, right = nums.length - 1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] >= target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}