var MAP = map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

func romanToInt(s string) (ans int) {
    n := len(s)
    for i := range s{
        val := MAP[s[i]]
        if i < n-1 && val < MAP[s[i+1]] {
            ans -= val
        }else{
            ans += val
        }
    }    
    return
}