package leetcode;

public class leetcode230 {
    private int k;
    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        return dfs(root);

    }
    private int dfs(TreeNode node) {
        if(node == null) return -1;
        int left = dfs(node.left);
        if(left != -1) return left;
        if(--k == 0) return node.val;
        return dfs(node.right);
    }
}
