//  What if our data stream is really big?
//  I don't know! I just figured it out if the first 7 digits
// represent a number > half the length of the total signal :)

package main

import (
	"fmt"
	"io/ioutil"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func numberRead(brokenNumber []int) int {
	answer := 0
	for _, value := range brokenNumber {
		answer = answer * 10 + value
	}
	return answer
}

func readFile(fileLocation string) []int {
	fContent, err := ioutil.ReadFile(fileLocation)
	if err != nil {
		fmt.Print(err)
	}

	var result []int
	for _, char := range fContent {
		if int(char-48) >= 0 && int(char-48) <= 9 {
			result = append(result, int(char-48))
		}
	}

	longResult := result
	for i := 1; i < 10000; i++ {
		longResult = append(longResult, result...)
	}
	
	return longResult
}

func abbreviatedCycle(signal []int, pattern []int, starter int) []int {
	base := 0
	result := make([]int, len(signal))
	copy(result, signal)
	for i := len(signal)-1; i >= starter; i-- {
		if i >= len(signal) / 2 {
			base += signal[i]
			result[i] = abs(base) % 10
		} else if i < len(signal) / 2 {
			fmt.Println("Bummer, gotta write this")
		}
	}

	return result
}

func main() {
	signal := readFile("input.txt")
	starter := numberRead(signal[:7])
	fmt.Println(starter)
	for i := 0; i < 100; i++ {
		signal = abbreviatedCycle(signal, []int{0, 1, 0, -1}, starter)
	}
	fmt.Println(signal[starter:starter+8])
}
