class Solution {
    private record Pair(String s, int k) {
    }

    public String decodeString(String s) {
        Deque<Pair> stack = new ArrayDeque<>(); // 用于模拟计算机的递归
        StringBuilder res = new StringBuilder();
        int k = 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                res.append(c);
            } else if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                // 模拟递归
                // 在递归之前，把当前递归函数中的局部变量 res 和 k 保存到栈中
                stack.push(new Pair(res.toString(), k));
                // 递归，初始化 res 和 k
                res.setLength(0);
                k = 0;
            } else { // ']'
                // 递归结束，从栈中恢复递归之前保存的局部变量
                Pair p = stack.pop();
                // 此时 res 是下层递归的返回值，将其重复 p.k 次，拼接到递归前的 p.s 之后
                res = new StringBuilder(p.s).repeat(res, p.k);
            }
        }
        return res.toString();
    }
}

