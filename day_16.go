//  Processing data streams to get results

package main

import (
	"fmt"
	"math"
	"io/ioutil"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func customMod(add int, modulo int) int {
	return int(math.Mod(float64(add), float64(modulo)))
}

func readFile(fileLocation string) string {
	fContent, err := ioutil.ReadFile(fileLocation)
	if err != nil {
		fmt.Print(err)
	}

	return string(fContent)
}

func signalTransform(str string) []int {
	var result []int
	for _, char := range str {
		if int(char-48) >= 0 && int(char-48) <= 9 {
			result = append(result, int(char-48))
		}
	}
	longResult := result
	//for i := 0; i < 10000; i++ {
	//	longResult = append(longResult, result...)
	//}
	return longResult
}

func oneCycle(signal []int, pattern []int) []int {
	computeSignal := make([]int, len(signal))
	for i := 0; i < len(signal); i++ {
		count := 0
		result := 0
		for j := i; j < len(signal); j++ {
			if (j - i) % (i + 1) == 0 {
				count = customMod(count+1, len(pattern))
			}
			result += signal[j] * pattern[count]
		}
		computeSignal[i] = abs(result) % 10
	}

	return computeSignal
}

func main() {
	signal := readFile("input.txt")
	intSignal := signalTransform(signal)
	for i := 0; i < 100; i++ {
		intSignal = oneCycle(intSignal, []int{0,1,0,-1})
	}
	fmt.Println(intSignal[:8])
}
