class Solution {
    public boolean canPartition(int[] nums) {
        int s = 0;
        for(int num:nums){
            s += num;
        }
        if(s % 2 != 0) return false;
        s /= 2;
        boolean[] f = new boolean [s + 1];
        f[0] = true;
        int s2 = 0;
        for(int x:nums){
            s2 = Math.min(s2 + x, s);
            for(int i = s2; i >= x; i--){
                f[i] = f[i] || f[i - x];
            }
            if(f[s]) return true;
        }
        return false;
    }
}