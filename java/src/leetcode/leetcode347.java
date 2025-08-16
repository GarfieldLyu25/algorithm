class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> hash = new HashMap<>();
        for(int num:nums){
            hash.merge(num,1,Integer::sum);
            //hash.put(num, hash.getOrDefault(num, 0) + 1);
        }
        int maxCnt = Collections.max(hash.values());
        List<Integer>[] buckets = new ArrayList[maxCnt + 1];
        Arrays.setAll(buckets, i -> new ArrayList<>());
        for(Map.Entry<Integer, Integer> e : hash.entrySet()){
            buckets[e.getValue()].add(e.getKey());
        }
        int[] ans = new int[k];
        int j = 0;
        for (int i = maxCnt; i >= 0 && j < k; i--) {
            for (int x : buckets[i]) {
                ans[j++] = x;
            }
        }
        return ans;
    }
}