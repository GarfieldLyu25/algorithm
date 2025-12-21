func productExceptSelf(nums []int) []int {
    n := len(nums)
    suf := make([]int,n)
    suf[n-1] = 1
    for i := n-2 ; i >= 0; i-- {
        suf[i] = suf[i+1] * nums[i+1]
    }
    pre := 1
    for i := 0 ; i < n ;i++ {
        suf[i] *= pre
        pre *= nums[i]
    }
    return suf
}