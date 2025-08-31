class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Deque<Integer> st = new ArrayDeque<>();
        int[] ans = new int[n];
        for(int i = n - 1;i >= 0; i--){
            int t = temperatures[i];
            while(!st.isEmpty() && t >= temperatures[st.peek()]) {
                st.pop();
            }
            if(!st.isEmpty()){
                ans[i] = st.peek() - i;
            }
            st.push(i);
        }
        return ans;
    }
}