class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] g = new ArrayList[numCourses];
        Arrays.setAll(g, i -> new ArrayList<>());
        for(int[] p:prerequisites){
            g[p[1]].add(p[0]);
        }
        int[] colors = new int[numCourses];
        for(int i = 0; i < numCourses; i++){
            if(colors[i]  == 0 && dfs(i,g,colors)){
                return false; //有环
            }
        }
        return true;
    }

    //true 有环
    private boolean dfs(int x,List<Integer>[] g, int[] colors){
        colors[x] = 1; // x 正在访问中
        for(int y:g[x]){
            if(colors[y] == 1 || colors[y] == 0 && dfs(y,g,colors)){
                return true;
            }
        }
        colors[x] = 2;
        return false;
    }
}