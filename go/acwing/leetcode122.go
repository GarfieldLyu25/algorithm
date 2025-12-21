package main

import "fmt"

func maxProfit(prices []int) (int) {
	for i := 1; i < len(prices); i++ {
		ans += max(0, prices[i]-prices[i-1])
	}
	return ans
}

func main() {
	prices := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	ans := 0
	ans = maxProfit(prices)
	fmt.Println(ans)
}
