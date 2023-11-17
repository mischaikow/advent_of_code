//  Decided to try this one in Go
//  First time using the language, pretty fun!

package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
	"strconv"
	"math"
)

type Chemical struct {
	name string
	coef int
}

func strToChem(reagent string) Chemical {
	cut := strings.Split(reagent, " ")
	theCoef, err := strconv.Atoi(cut[0])
	if err != nil {
		log.Fatal(err)
	}
	return Chemical{cut[1], theCoef}
}

type Reaction struct {
	output Chemical
	input []Chemical
}

func parseLine(aLine string) Reaction {
	cutLine := strings.Split(aLine, " => ")
	inputCut := strings.Split(cutLine[0], ", ")

	output := strToChem(cutLine[1])
	var input []Chemical
	for _, value := range inputCut {
		input = append(input, strToChem(value))
	}
	
	return Reaction{output, input}
}

func readFile(fileLocation string) map[string]Reaction {
	fContent, err := os.Open(fileLocation)
	if err != nil {
		log.Fatal(err)
	}

	allReactions := make(map[string]Reaction)
	
	s := bufio.NewScanner(fContent)
	for s.Scan() {
		aReaction := parseLine(s.Text())
		allReactions[aReaction.output.name] = aReaction
	}
	return allReactions
}

func computeOre(allReactions map[string]Reaction, fuelCount int) int {
	theChems := make(map[string]int)
	for key, _ := range allReactions {
		theChems[key] = 0
	}
	theChems["FUEL"] = fuelCount
	theChems["ORE"] = 0

	reactChain(allReactions, theChems, "FUEL")

	return theChems["ORE"]
}

func reactChain(allReactions map[string]Reaction, theChems map[string]int, aChem string) {
	if aChem == "ORE" {return}
	thisReaction := allReactions[aChem]
	outChemVal := thisReaction.output.coef
	inputs := thisReaction.input

	reactionCount := int(math.Ceil(float64(theChems[aChem]) / float64(outChemVal)))
	theChems[aChem] -= reactionCount * outChemVal

	for _, value := range inputs {
		theChems[value.name] += value.coef * reactionCount
	}
	
	for _, value := range inputs {
		reactChain(allReactions, theChems, value.name)
	}
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	allReactions := readFile("input.txt")

	ratio := computeOre(allReactions, 1)
	fmt.Println("The ore needed for one unit of fuel is:", ratio)

	guess := 1000000000000 / ratio
	
	for temp := ratio; Abs(temp) > 0; {
		
		temp = (computeOre(allReactions, guess) - 1000000000000) / ratio
		guess -= temp
	}

	fmt.Println(guess)
}
