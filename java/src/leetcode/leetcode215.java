public class Solution {
    int quickselect(int[] nums, int l, int r, int k) {
        while(true){
            if (l == r) return nums[l];
            int x = nums[l + r >> 1], i = l - 1, j = r + 1;
            while (i < j) {
                do i++; while (nums[i] > x);
                do j--; while (nums[j] < x);
                if (i < j){
                    int tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                }
            }
            // 2   1
            // lij  r
            if (k <= j - l + 1) r = j;
            else {
                k = k - (j - l + 1);
                l = j + 1;
            }
        }
    }
    //从大到小排
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        return quickselect(nums, 0, n - 1, k);
    }
}
//1
//1 2