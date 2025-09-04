class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int n = candidates.length;
        boolean[][] f = new boolean[n + 1][target + 1];
        f[0][0] = true;
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= target; j++){ //
                f[i + 1][j] = f[i][j] || (j >= candidates[i] && f[i + 1][j -  candidates[i]]);
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(n - 1, target, candidates, f, ans, path);
        return ans;
    }
    private void dfs(int i,int left, int[] candidates, boolean[][] f, List<List<Integer>> ans, List<Integer> path){
        if(left == 0){
            ans.add(new ArrayList<>(path));   //new一个
            return;
        }
        if(left < 0 || !f[i + 1][left]){
            return;
        }

        dfs(i - 1, left, candidates, f, ans, path);

        path.add(candidates[i]);
        dfs(i, left - candidates[i], candidates, f, ans, path); //可以重复选
        path.remove(path.size() - 1);
    }
}


// 在Java中，对象是通过引用传递的。如果我们直接将path对象添加到ans列表中（即使用ans.add(path)），
// 那么ans中存储的将是path对象的引用，而不是其内容的副本。随后，当path对象在回溯过程中被修改（例如
// 通过path.remove(path.size() - 1)），ans中已添加的列表也会随之改变，因为它们实际上是同一个
// 对象。这会导致最终ans中的所有列表都指向同一个path对象，从而内容相同且为最后一次修改的状态。