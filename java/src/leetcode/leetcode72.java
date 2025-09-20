class Solution {
    public int minDistance(String text1, String text2) {
        char[] s = text1.toCharArray();
        char[] t = text2.toCharArray();
        int n = s.length;
        int m = t.length;
        int[][] f = new int[n + 1][m + 1];
        for (int j = 0; j < m; j++) {
            f[0][j + 1] = j + 1;
        }
        for (int i = 0; i < n; i++) {
            f[i + 1][0] = i + 1;
            for (int j = 0; j < m; j++) {
                f[i + 1][j + 1] = s[i] == t[j] ? f[i][j] :
                        Math.min(Math.min(f[i][j + 1], f[i + 1][j]), f[i][j]) + 1;
            }
        }
        return f[n][m];
    }
}
